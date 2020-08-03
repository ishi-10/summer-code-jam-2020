from rest_framework import serializers
from fbbackend import models

'''
Serializers for the "Model" objects located in Models.py
'''

class AccountSerializer(serializers.ModelSerializer): #Serializer for accounts
    class Meta:
        model = models.Account
        fields = ('email', 'hashed_pass', 'nickname', 'bot', 'identification')

class MessageSerializer(serializers.ModelSerializer): #Serializer for Messages
    class Meta:
        model = models.Message
        fields = ('writer', 'content', 'identification')


class GroupSerializer(serializers.ModelSerializer): #Serializer for Groups
    class Meta:
        model = models.Group
        fields = ('creator', 'messages', 'name', 'identification')


class PostSerializer(serializers.ModelSerializer): #Serializer for Posts
    class Meta:
        model = models.Post
        fields = ('creator', 'content', 'title', 'comments', 'identification')


