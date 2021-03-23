from django.shortcuts import render
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import csv,json
import requests


# connect to our Redis instance
redis_instance = redis.Redis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT)



@api_view(['GET'])
def manage_item(request,**kwargs):
    print("okay+++++++++++++++++++++")
    print("get req",(request.GET.get("value")))
    item = (request.GET.get("value")).upper()
    print("item",item)
    if request.GET.get("value") is not None:
        searchKey = '*'+item+'*';
        print(searchKey)
        values = redis_instance.keys(searchKey)
        print("value",len(values))
        if len(values) != 0:
            AllkeyList = []
            count = 0
            for key in values:
                print("key",key)
                dict = {}
                getValue = redis_instance.hmget(key,"open","high","low","close"),
                print(getValue[0][0],(getValue))
                dict["keyname"] = key
                dict["open"] = getValue[0][0]
                dict["high"] = getValue[0][1]
                dict["low"] = getValue[0][2]
                dict["close"] = getValue[0][3]
                print("dict",dict)
                count = count+1
                AllkeyList.append(dict)
            
            response = {
                'key': item,
                'SearchResults' : AllkeyList,
                'msg': 'success'
            }
            print("AllkeyList",AllkeyList)
            return Response(response, status=200)
        else:
            response = {
                'key': item,
                'SearchResults': None,
                'msg': 'Not found'
            }
            return Response(response, status=404)
    return "okay"