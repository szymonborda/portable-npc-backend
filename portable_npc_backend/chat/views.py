from django.shortcuts import render
from portable_npc_backend.chat import serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import generics
import openai

class ChatCompletionViewSet(generics.CreateAPIView, GenericViewSet):
    serializer_class = serializers.ChatCompletionSerializer

    def create(self, request):
        serializer = serializers.ChatCompletionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.validated_data
        openai.api_key = serialized_data['openai_api_key']
        system_message = {
            'role': 'system',
            'content': f'You are an NPC in a RPG game. Be creative and make stuff up. Always reply as you are a character with the following description: {serialized_data["context"]}',
        }
        messages = [system_message] + serialized_data['messages']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return Response({
            'message': response.choices[0].message, 
        })
