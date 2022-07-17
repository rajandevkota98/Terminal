from rest_framework import serializers
from django.core.exceptions import ImproperlyConfigured

from storemanagement.models import Company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        field = ["name","license_no","address", "contact_no","email","description"]
        exclude = ("name","license_no","address", "contact_no","email","description")
