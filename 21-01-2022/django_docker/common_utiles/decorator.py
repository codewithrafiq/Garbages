from functools import wraps
from django.db import connections
from django.conf import settings
import os



# def company_database(func):
#     """Checks company domain & user then switches the database"""
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         try:
#             domain = args[1].context.META.get('HTTP_DOMAIN')
#             print("Domain: {}".format(domain))
#             user = args[1].context.user
#             print("User: {}".format(user))
#         except AttributeError:
#             domain = args[2].context.META.get('HTTP_DOMAIN')
#             print("Domain: {}".format(domain))
#             user = args[2].context.user
#             print("User: {}".format(user))
#         if domain is None:
#             raise GraphQLError("Please provide company domain!")

#         company = Company.objects.filter(domain=domain).first()
#         if company is None:
#             raise GraphQLError("Provided company domain doesn't exist!")

#         if user is None:
#             raise GraphQLError("No user data provided!")
#         print("User ID: {}".format(user.id))

#         db = CompanyDatabase.objects.filter(company=company).first()
#         if db is None:
#             raise GraphQLError("No database found!")

#         new_database = {}
#         if 'test' in sys.argv:
#             new_database['ENGINE'] = 'django.db.backends.sqlite3'
#             new_database['NAME'] = db.db_name
#         else:
#             new_database['ENGINE'] = config('DATABASE_ENGINE', cast=str)
#             new_database['NAME'] = db.db_name
#             new_database['USER'] = config('DATABASE_USER', cast=str)
#             new_database['PASSWORD'] = config('DATABASE_PASSWORD', cast=str)
#             new_database['HOST'] = config('DATABASE_HOST', cast=str)
#             new_database['PORT'] = config('DATABASE_PORT', cast=int)
#         connections.databases[db.db_name] = new_database
#         print("Company DB: {}".format(db.db_name))
#         try:
#             check_user = CompanyUsers.objects.using(db.db_name).filter(user_id=user.id).first()
#         except Exception:
#             raise GraphQLError("No purchased modules found!")

#         if check_user is None:
#             raise GraphQLError("User not found!")

#         kwargs['db'] = db.db_name
#         kwargs['user'] = check_user

#         return func(*args, **kwargs)

#     return wrap


def my_database(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            user = args[1].user
        except AttributeError:
            user = args[2].user

        if user is None:
            raise Exception("No user data provided!")


        new_database = {}
        new_database['ENGINE'] = 'django.db.backends.sqlite3'
        new_database['NAME'] = os.path.join(settings.BASE_DIR, 'users_databases', f'{user.username}.db')
        connections.databases[user.username] = new_database

        kwargs['db'] = user.username
        kwargs['user'] = user

        return func(*args, **kwargs)

    return wrap


class SwitchDatabase:

    @classmethod
    def switch(self, db_name):
        newDatabase = {}

        newDatabase['ENGINE'] = 'django.db.backends.sqlite3'
        newDatabase['NAME'] = os.path.join(settings.BASE_DIR, 'users_databases', f'{db_name}.db')
        
        connections.databases[db_name] = newDatabase



################ Shashine Vhai ######################
from functools import wraps
from django.shortcuts import redirect

def usertype_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        print("request.user----------------->",request.user)
        return func(*args, **kwargs)
    return wrapper

def if_log_then_go(my_view):
    def check_authenticate(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return my_view(request, *args, **kwargs)
    return check_authenticate

def my_permission_chk(prem_str):
    def view_para(my_view):
        def check_permission(request, *args, **kwargs):
            if request.user.has_perm(prem_str):
                return my_view(request, *args, **kwargs)
            else:
                print("\t\t\t\t ",request.user," No Permission")
                #def list(self, request, *args, **kwargs):
                #    return Response({"error":"You has no Permission."})
                return redirect('User Log-In') # worked
                #def get(self):
                #    return Response({"error":"You has no Permission."})
        return check_permission
    return view_para
