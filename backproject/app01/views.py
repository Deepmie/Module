from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Customed_User,User
import json
# Create your views here.
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User # 针对Basic_User表进行序列化
        fields="__all__"
        # exclude=["pub_date"]
    # 加上后密码将不会显式地显示出来
    # def create(self,valid_data):
    #     return User.objects.create_user(**valid_data)
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self,instance,validated_data):
        user = super().update(instance,validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customed_User # 针对Basic_User表进行序列化
        fields="__all__"
        # exclude=["pub_date"]
    # def create(self,valid_data):
    #     return User.objects.create_user(**valid_data)

class CustomUserView(ModelViewSet):
    queryset=Customed_User.objects.all()
    serializer_class=CustomUserSerializers


@api_view(('GET','POST',))
# @renderer_classes((JSONRenderer))
def test(request):
    if request.method=='GET':
        print(request.method+' 请求发送成功')
        getData=dict(request.GET)
        print(getData)
        getStr=""
        for key,value in getData.items():
            getStr+=key+'='+str(value[0])+'&'
        getStr=getStr[0:-1]
        info='您使用'+request.method+'请求发送了'+getStr
        return Response(data=info)
    else :
        print(request.data)
        info='您使用'+request.method+'请求发送了'+json.dumps(request.data)
        return Response(data=info)
        # getData=dict(request.POST)
        # print(getData)
        # getStr=""
        # for key,value in getData.items():
        #     getStr+=key+'='+str(value[0])+'&'
        # getStr=getStr[0:-1]
        # info='您使用'+request.method+'请求发送了'+getStr
        # return Response(data=info)
