from .models import csvmodel,valueModel
import csv
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer, dataserializer, csvserializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .forms import csvModelForm
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.response import Response
import jwt, datetime
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class getdata(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = valueModel.objects.all()
        serializer = dataserializer(data,many = True)
        return Response(serializer.data)


    def post(self, request):
        csvfile = csvserializer(data=request.data)
        csvfile.is_valid(raise_exception=True)
        csvfile.save()
        return HttpResponse("done")         


def uploadfile(request):
    form = csvModelForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            form = csvModelForm()
            obj = csvmodel.objects.latest('id')
            with open(obj.file_upload.path, 'r') as f:
                reader = list(csv.reader(f))
                print("########################" + str(reader))
                for i, row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        if len(row[1])!=10 or not  (row[1][:].isnumeric()) :
                            print(row[1]  + " this phone number was wrong")
                        else:
                            valueModel.objects.create(
                                name=row[0],
                                phoneNumber=row[1]
                            )
    else:
        return HttpResponse("please login again via admin page you are logged out")
    return render(request, 'upload.html' ,{'form':form})


#to be used further for token generation for api
class ObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

