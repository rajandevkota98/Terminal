from django.contrib import admin
from stockmanagement.models import Company,Inventory,Employee,Customer,Bill,EmployeeSalary,BillDetails,CustomerRequest,CompanyAccount,CompanyBank,EmployeeBank
# Register your models here.
admin.site.register(Company)
admin.site.register(Inventory)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)
