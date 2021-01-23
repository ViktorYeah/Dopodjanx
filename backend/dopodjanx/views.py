from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dopodjanx.models import CompanyInfo
from dopodjanx.serializers import CompanyInfoSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def companiesApi(request, id=0):
    if request.method == 'GET':
        companies = None
        if id == 0:
            companies = CompanyInfo.objects.all()
        else:
            companies = CompanyInfo.objects.filter(Id=id)

        company_info_serializer = CompanyInfoSerializer(companies, many=True)

        return JsonResponse(company_info_serializer.data, safe=False)
    elif request.method=='POST':
        companies_data=JSONParser().parse(request)
        companies_serializer = CompanyInfoSerializer(data=companies_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        companies_data = JSONParser().parse(request)
        companyInfo = CompanyInfo.objects.get(Id=companies_data['Id'])
        companies_serializer = CompanyInfoSerializer(companyInfo, data=companies_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse('Updated Successfully!', safe=False)
            
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        companyInfo = CompanyInfo.objects.get(Id=id)
        companyInfo.delete()
        return JsonResponse('Deleted Successfully!!', safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
