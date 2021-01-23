from rest_framework import serializers
from dopodjanx.models import CompanyInfo

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ('Id', 'Name', 'DateTime', 'Employees', 'Assets', 'Link')