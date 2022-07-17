from rest_framework import  serializers

from stockmanagement.models import Company, CompanyBank, Inventory,Employee,EmployeeSalary,EmployeeBank,CustomerRequest,Customer,CompanyAccount,Bill,BillDetails

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        field = "__all__"
        exclude = ("added_on",)

class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        field = "__all__"
        exclude = ("added_on",)
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.company_id).data
    #     return  response


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        field = "__all__"
        exclude = ("added_on",)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        field = "__all__"
        exclude = ("added_on",)



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field = "__all__"
        exclude = ("added_on",)

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        field = "__all__"
        exclude = ()
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer_id).data
        return response


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        field = "__all__"
        exclude = ("added_on","status",)

class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        field = "__all__"
        exclude = ()
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        field = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        field = "__all__"
        exclude = ()

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = BillSerializer(instance.bill_id).data
        return response


class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        field = "__all__"
        exclude = ()
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.company_id).data
    #     return response




