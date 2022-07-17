from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework import viewsets
from stockmanagement.models import Company, CompanyBank, Inventory, CompanyAccount, Employee, EmployeeBank, \
    EmployeeSalary, CustomerRequest, Bill, BillDetails
from rest_framework.generics import get_object_or_404
from stockmanagement.serializers import CompanySerializer, CompanyBankSerializer, InventorySerializer, \
    CompanyAccountSerializer, EmployeeSerializer, EmployeeBankSerializer, EmployeeSalarySerializer, CustomerSerializer, \
    BillSerializer, BillDetailsSerializer, CustomerRequestSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import permissions


# Create your views here.
class CompanyViewSet(viewsets.ViewSet):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        def list(self, request):
                company = Company.objects.all()
                serializer = CompanySerializer(company, many=True, context={"request": request})
                response_dict = {"error": False, "message": "All Company Data", "data": serializer.data}
                return Response(response_dict)

        def create(self, request):
                try:
                    serializer = CompanySerializer(data = request.data, context={"request":request})
                    serializer.is_valid(raise_exception= True)
                    serializer.save()
                    dict_response = {"error":False, "message":"Company data has been saved"}
                except:
                    dict_response = {"error":True, "message":"error in saving"}
                return Response(dict_response)


        def update(self, request, pk=None):
            try:
                queryset = Company.objects.all()
                company = get_object_or_404(queryset, pk=pk)
                serializer = CompanySerializer(company,data = request.data, context={"request":request})
                serializer.is_valid(raise_exception= True)
                serializer.save()
                dict_response = {"error": False, "message": "Company data has been updated"}
            except:
                dict_response = {"error": True, "message": "Company data coundn't  bee updated"}
            return Response(dict_response)

        def retrieve(self, request, pk=None):
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, context={"request": request})

            serializer_data = serializer.data

            company_bank_details = CompanyBank.objects.filter(company_id=serializer_data["id"])
            companybank_details_serializers = CompanyBankSerializer(company_bank_details, many=True)
            serializer_data["company_bank"] = companybank_details_serializers.data

            return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

        def delete(self, request, pk=None):
            try:
                queryset = Company.objects.all()
                company = get_object_or_404(Company, pk=pk)
                # serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
                # serializer.is_valid(raise_exception=True)
                company.delete()
                dict_response = {"error": False, "message": "Company  data has been deleted."}
            except:
                dict_response = {"error": True, "message": "company data coundn't  be deleted."}
            return Response(dict_response)





class InventoryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=InventorySerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)


            # inventory_list = []
            serializer.save()
            inventory_id = serializer.data['id']

            dict_response={"error":False,"message":"Product Data has been  Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Product Data"}
        return Response(dict_response)

    def list(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All product data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = Inventory.objects.all()
        inventory = get_object_or_404(queryset, pk =pk)
        serializer= InventorySerializer(inventory, context={"request":request})
        return Response({"error":False, "message":"Single data is fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Inventory.objects.all()
            inventory = get_object_or_404(queryset, pk=pk)
            serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Product  data has been updated"}
        except:
            dict_response = {"error": True, "message": "Product data coundn't  be update"}
        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            queryset = Inventory.objects.all()
            inventory = get_object_or_404(Inventory, pk=pk)
            # serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
            # serializer.is_valid(raise_exception=True)
            inventory.delete()
            dict_response = {"error": False, "message": "Product  data has been deleted."}
        except:
            dict_response = {"error": True, "message": "Product data coundn't  be deleted."}
        return Response(dict_response)




class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer
    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.objects.filter(name =name)


class CompanyonlyViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

    # Creating new viewset for others


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=CompanyBankSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Company Bank Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Bank Data"}
        return Response(dict_response)

    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(companybank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk =pk)
        serializer= CompanyBankSerializer(companybank, context={"request":request})
        return Response({"error":False, "message":"Single data is fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company data has been updated"}
        except:
            dict_response = {"error": True, "message": "Company data coundn't  be updated"}
        return Response(dict_response)



    def delete(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(CompanyBank, pk=pk)
            # serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
            # serializer.is_valid(raise_exception=True)
            companybank.delete()
            dict_response = {"error": False, "message": "bank  data has been deleted."}
        except:
            dict_response = {"error": True, "message": "bank data coundn't  be deleted."}
        return Response(dict_response)





class CompanyAccountViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=CompanyAccountSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Company Account Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Account Data"}
        return Response(dict_response)

    def list(self, request):
        companyaccount = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(companyaccount, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = CompanyAccount.objects.all()
        companyaccount = get_object_or_404(queryset, pk =pk)
        serializer= CompanyAccountSerializer(companyaccount, context={"request":request})
        return Response({"error":False, "message":"Single account is fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyAccount.objects.all()
            companyaccount = get_object_or_404(queryset, pk=pk)
            serializer = CompanyAccountSerializer(companyaccount, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Account data has been updated"}
        except:
            dict_response = {"error": True, "message": "Account data coundn't  be updated"}
        return Response(dict_response)





class EmployeeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=EmployeeSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Employee Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving EmployeeData"}
        return Response(dict_response)

    def list(self, request):
        employeedata = Employee.objects.all()
        serializer = EmployeeSerializer(employeedata, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All employee Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = Employee.objects.all()
        employeedata = get_object_or_404(queryset, pk =pk)
        serializer= EmployeeSerializer(employeedata, context={"request":request})
        return Response({"error":False, "message":"Single account of employee fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employeedata = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employeedata, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Account data has been updated"}
        except:
            dict_response = {"error": True, "message": "Account data coundn't  be updated"}
        return Response(dict_response)
    def delete(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employeedata = get_object_or_404(Employee, pk=pk)
            # serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
            # serializer.is_valid(raise_exception=True)
            employeedata.delete()
            dict_response = {"error": False, "message": "Employee  data has been deleted."}
        except:
            dict_response = {"error": True, "message": "Employee data coundn't  be deleted."}
        return Response(dict_response)





class EmployeeBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=EmployeeBankSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Employee Bank  Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving employee bank data EmployeeData"}
        return Response(dict_response)

    def list(self, request):
        employeebank = EmployeeBank.objects.all()
        serializer = EmployeeBankSerializer( employeebank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All employee bank Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = EmployeeBank.objects.all()
        employeebank = get_object_or_404(queryset, pk =pk)
        serializer= EmployeeBankSerializer( employeebank, context={"request":request})
        return Response({"error":False, "message":"Single account of employee fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            employeebank = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializer( employeebank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee bank  data has been updated"}
        except:
            dict_response = {"error": True, "message": "Employee bank data coundn't  be updated"}
        return Response(dict_response)




class EmployeeSalaryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=EmployeeSalarySerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Employee salary  Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving employee salary data EmployeeData"}
        return Response(dict_response)

    def list(self, request):
        employeeSalary = EmployeeSalary.objects.all()
        serializer = EmployeeSalarySerializer( employeeSalary, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All employee bank Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request,pk=None):
        queryset = EmployeeSalary.objects.all()
        employeeSalary = get_object_or_404(queryset, pk =pk)
        serializer= EmployeeSalarySerializer( employeeSalary, context={"request":request})
        return Response({"error":False, "message":"Single account of employee fetched","data":serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            employeeSalary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializer( employeeSalary, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Employee bank  data has been updated"}
        except:
            dict_response = {"error": True, "message": "Employee bank data coundn't  be updated"}
        return Response(dict_response)


class EmployeebankByidViewSet(generics.ListAPIView):
    serializer_class = EmployeeBankSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        return EmployeeBank.objects.filter(employee_id =employee_id)

class BillgenerateViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = CustomerSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        customer_id = serializer.data['id']

        # we are creating for bill data to generate bill_id
        billdata = {}
        billdata["customer_id"] = customer_id;
        serializeranother = BillSerializer(data=billdata, context={"request": request})
        serializeranother.is_valid(raise_exception=True)
        serializeranother.save()
        bill_id = serializeranother.data['id']

        product_details_list = []
        for product_detail in request.data["product_details"]:
            product_detail1 = {}
            product_detail1["product_id"] = product_detail["id"]
            product_detail1["bill_id"] = bill_id
            product_detail1["qty"] = product_detail["qty"]

            product_deduct = Inventory.objects.get(id=product_detail["id"])
            print(product_detail)
            product_deduct.in_stock_total = int(product_deduct.in_stock_total) - int(product_detail['qty'])
            product_deduct.save()

            product_details_list.append(product_detail1)

        serializer3 = BillDetailsSerializer(data=product_details_list, many=True, context={"request": request})
        serializer3.is_valid()
        serializer3.save()

        dict_response = {"error": False, "message": "Bill Generate Successfully"}
        return Response(dict_response)





class EmployeesalaryByidViewSet(generics.ListAPIView):
    serializer_class = EmployeeSalarySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        return EmployeeSalary.objects.filter(employee_id =employee_id)



class InventoryNameViewSet(generics.ListAPIView):
    serializer_class = InventorySerializer
    def get_queryset(self):
        name = self.kwargs["name"]
        return Inventory.objects.filter(name__contains =name)


class HomeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        customer_request = CustomerRequest.objects.all()
        customer_serializer= CustomerRequestSerializer(customer_request, context={"request":request},many= True)
        # dict_response={"error":False, "message":"Message home page data has been displayed", "customer_request":len(customer_serializer.data)}
        # return Response(dict_response)
        total_bill = Bill.objects.all()
        total_bill_serializer = BillSerializer(total_bill, context={"request": request}, many=True)


        total_product = Inventory.objects.all()
        total_product_serializer= InventorySerializer(total_product,context={"request":request},many=True)

        total_company = Company.objects.all()
        total_company_serializer = CompanySerializer(total_company, context={"request": request}, many=True)

        total_employee_of_company = Employee.objects.all()
        total_employee_of_companyserializer = EmployeeSerializer(total_employee_of_company, context={"request": request}, many=True)

        #for tracking bill details
        all_bills = BillDetails.objects.all()
        profit= 0
        sell = 0
        buy= 0
        for bill in all_bills:
            buy = buy+int(bill.product_id.buy_price)*int(bill.qty)
            sell  = sell + int(bill.product_id.sell_price)*int(bill.qty)

        profit = sell - buy

        today = datetime.today().strftime("%Y-%m-%d")
        all_bills_today = BillDetails.objects.filter(added_on__date=today)
        profit_today = 0
        sell_today = 0
        buy_today = 0
        for bill_today in all_bills_today:
            buy_today = buy_today + int(bill_today.product_id.buy_price)*int(bill.qty)
            sell_today = sell_today + int(bill_today.product_id.sell_price)*int(bill.qty)

        profit_today = sell_today - buy_today
        current_date = datetime.today()
        after_a_month = current_date + timedelta(days=30)
        date_after_a_month = after_a_month.strftime("%Y-%m-%d")



        #getting product whose expiry date is in between 30 days
        product_expiry_date = Inventory.objects.filter(expire_date__range=[current_date, date_after_a_month])
        productExpireSerializer = InventorySerializer(product_expiry_date,many= True, context={"request":"request"})

        bill_dates = BillDetails.objects.order_by().values("added_on__date").distinct()
        profit_chart_list = []
        sell_chart_list = []
        buy_chart_list = []
        for billdate in bill_dates:
            access_date = billdate["added_on__date"]

            bill_data = BillDetails.objects.filter(added_on__date=access_date)
            profit_amt_inner = 0
            sell_amt_inner = 0
            buy_amt_inner = 0

            for billsingle in bill_data:
                buy_amt_inner = float(buy_amt_inner + float(billsingle.product_id.buy_price)) * int(billsingle.qty)
                sell_amt_inner = float(sell_amt_inner + float(billsingle.product_id.sell_price)) * int(billsingle.qty)

            profit_amt_inner = sell_amt_inner - buy_amt_inner

            profit_chart_list.append({"date": access_date, "amt": profit_amt_inner})
            sell_chart_list.append({"date": access_date, "amt": sell_amt_inner})
            buy_chart_list.append({"date": access_date, "amt": buy_amt_inner})
        # bill_dates = BillDetails.objects.order_by().values("added_on__date").distinct()
        # profit_chart_list = []
        # sell_chart_list =[]
        # buy_chart_list = []
        #
        # for billdate in bill_dates:
        #     date_access = billdate["added_on__date"]
        #     bill_data = BillDetails.objects.filter(added_on__date= date_access)
        #     profit_inner = 0
        #     sell_inner = 0
        #     buy_inner = 0
        #
        #     for single_bill in bill_data:
        #         buy_today_inner = buy_today_inner + int(single_bill.product_id.buy_price) * int(single_bill.qty)
        #         sell_today_inner = sell_today_inner + int(single_bill.product_id.sell_price) * int(single_bill.qty)
        #     profit_today_inner = sell_today_inner - buy_today_inner
        #     profit_chart_list.append({'date':date_access,'amount':profit_today_inner})
        #     sell_chart_list.append({'date':date_access,'amount':sell_today_inner})
        #     buy_chart_list.append({'date':date_access,'amount':buy_today_inner})








        dict_response = {"error": False, "message": "Message home page data has been displayed","productExpiring":  productExpireSerializer.data,   "productExpireSerializer_data":len(productExpireSerializer.data),"profit_today":profit_today,"sell_today":sell_today, "buy_today": buy_today,"sell_amount":sell, "buy_amount":buy,"profit":profit ,   "total_employee_of_company":len(total_employee_of_companyserializer.data),"total_company":len(total_company_serializer.data),"total_product":len(total_product_serializer.data),"customer_request":len(customer_serializer.data), "total_bill": len(total_bill_serializer.data),"sell_chart":sell_chart_list,"profit_chart":profit_chart_list,"buy_chart":buy_chart_list}
        return Response(dict_response)





class RequestViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        customer_request=CustomerRequest.objects.all()
        serializer=CustomerRequestSerializer(customer_request,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Customer Request Data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=CustomerRequestSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Customer Request Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Customer Request Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = CustomerRequest.objects.all()
        customer_request = get_object_or_404(queryset, pk=pk)
        serializer = CustomerRequestSerializer(customer_request, context={"request": request})

        serializer_data = serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=CustomerRequest.objects.all()
            customer_request=get_object_or_404(queryset,pk=pk)
            serializer=CustomerRequestSerializer(customer_request,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Customer Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Customer Data"}

        return Response(dict_response)
    def delete(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            customer_request = get_object_or_404(CustomerRequest, pk=pk)
            # serializer = InventorySerializer(inventory, data=request.data, context={"request": request})
            # serializer.is_valid(raise_exception=True)
            customer_request.delete()
            dict_response = {"error": False, "message": "Request  data has been deleted."}
        except:
            dict_response = {"error": True, "message": "Request data coundn't  be deleted."}
        return Response(dict_response)


company_list = CompanyViewSet.as_view({"get":"list"})
company_create = CompanyViewSet.as_view({"post":"create"})
company_update = CompanyViewSet.as_view({"put":"update"})