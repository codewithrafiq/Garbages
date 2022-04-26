from rest_framework import serializers
from .models import *





class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class EmployeeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeStatus
        fields = '__all__'

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'


class MenuPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPermission
        fields = '__all__'

class RoleMenuPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMenuPermission
        fields = '__all__'

class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermissions
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'


# ------------------------------------------------------------

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'

class DesignationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designations
        fields = '__all__'

class GeneratedSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedSalary
        fields = '__all__'

class AttendanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatus
        fields = '__all__'

class BonusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusTypes
        fields = '__all__'


class ScalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scales
        fields = '__all__'

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'

class AttendancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendances
        fields = '__all__'

class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'