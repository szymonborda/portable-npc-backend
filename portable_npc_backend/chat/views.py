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
        openai.api_key = serialized_data["openai_api_key"]
        system_message = {
            "role": "system",
            "content": f'You are an NPC called "{serialized_data["name"]}" in an RPG game. Be creative, make stuff up, and make the game interesting and fun. Always reply as you are a character with the following description: "{serialized_data["context"]}"',
        }
        messages = [system_message] + serialized_data["messages"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return Response(
            {
                "message": response.choices[0].message,
            }
        )


class ChatCharacterViewSet(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
    GenericViewSet,
):
    serializer_class = serializers.ChatCharacterSerializer

    def get_queryset(self):
        return self.request.user.chat_characters.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
