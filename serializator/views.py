from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from rest_framework.utils import serializer_helpers
from serializator.models import Meteor
from serializator.api.serializers import MeteorSerializer


@csrf_exempt
def meteor_list(request):
    # List all code meteor, or create a new meteor
    if request.method == 'GET':
        meteor = Meteor.objects.all()
        serializer = MeteorSerializer(meteor, many=True)
        return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MeteorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, satus=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def meteor_detail(request, pk):
    # Retrieve, update or delete a code meteor
    try:
        meteor = Meteor.object.get(pk=pk)
    except Meteor.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = MeteorSerializer(meteor)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MeteorSerializer(meteor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer)
    elif request.method == 'DELETE':
        meteor.delete()
        return HttpResponse(status=204)