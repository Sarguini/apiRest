# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from serializator.models import Meteor


class MeteorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meteor
        fields = ['id', 'name', 'weight', 'image', 'price']
