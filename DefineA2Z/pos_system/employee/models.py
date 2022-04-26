from email.policy import default
from lib2to3.pytree import Base
from pyexpat import model
from statistics import mode
from django.db import models
from pyparsing import java_style_comment
from common_utils.BaseClass import BaseModel
from django.contrib.auth.models import User

class Shops(BaseModel):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    logo = models.TextField()
    favi_icon = models.TextField()
    address = models.TextField(default=dict)

    def __str__(self):
        return self.title


class Branches(BaseModel):
    name = models.CharField(max_length=100)
    address = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Socials(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name

class Roles(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class EmployeeStatus(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_join = models.BooleanField(default=False)
    note = models.TextField(default='')

class Menus(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class Permissions(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

class MenuPermission(BaseModel):
    menu_id = models.ForeignKey(Menus, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    

class RoleMenuPermission(BaseModel):
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    menu_permission_id = models.ForeignKey(MenuPermission, on_delete=models.CASCADE)


class UserPermissions(BaseModel):
    menu_permission_id = models.ForeignKey(MenuPermission, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Customers(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()


class Suppliers(BaseModel):
    company_name = models.CharField(max_length=100)
    logo = models.TextField()
    contact_person = models.CharField(max_length=100)
    address = models.TextField()
    contacts = models.TextField()
    accounts = models.JSONField(default=dict)


#---------------------------------------------------------------------------------------------------------------------- 




class Grades(BaseModel):
    name = models.CharField(max_length=100)


class Designations(BaseModel):
    name = models.CharField(max_length=100)

class GeneratedSalary(BaseModel):
    branch_id = models.ForeignKey(Branches, on_delete=models.CASCADE)
    month = models.DateField()
    scale_id = models.IntegerField()

class AttendanceStatus(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    attendance_status_id = models.IntegerField()


class BonusTypes(BaseModel):
    name = models.CharField(max_length=100)

class Scales(BaseModel):
    branch_id = models.ForeignKey(Branches, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grade_id = models.ForeignKey(Grades, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    transport_cost = models.FloatField()
    cut_transport_cost_per_day_absent = models.FloatField()
    house_rent = models.FloatField()
    cut_house_rent = models.FloatField()
    medical_allownce = models.FloatField()
    cut_medical_allowance = models.FloatField()
    mobile_bill = models.FloatField()
    cut_mobile_bill = models.FloatField()

class Bonus(BaseModel):
    scale_id = models.IntegerField()
    bonus_type_id = models.ForeignKey(BonusTypes, on_delete=models.CASCADE)
    type = models.IntegerField()
    bonus = models.IntegerField()
    amount = models.FloatField()
    bonus_month = models.DateField()


class Attendances(BaseModel):
    name = models.CharField(max_length=100)

class Salaries(BaseModel):
    branch_id = models.ForeignKey(Branches, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    grade_id = models.ForeignKey(Grades, on_delete=models.CASCADE)
    scale_id = models.ForeignKey(Scales, on_delete=models.CASCADE)
    month = models.CharField(max_length=100)
    total_days = models.IntegerField()
    total_absent = models.IntegerField()
    total_present = models.IntegerField()
    basic_salary = models.FloatField()
    transport_cost = models.FloatField()
    cut_transport_cost = models.FloatField()
    house_rent = models.FloatField()
    cut_house_rent = models.FloatField()
    medical_allowance = models.FloatField()
    cut_medical_allowance = models.FloatField()
    mobile_bill = models.FloatField()
    cut_mobile_bill = models.FloatField()
    bonus_id = models.ForeignKey(Bonus, on_delete=models.CASCADE)
    bonus = models.FloatField()
    total = models.FloatField()