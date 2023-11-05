from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=['function', 'system', 'user', 'assistant'])
    content = serializers.CharField()

class ChatCompletionSerializer(serializers.Serializer):
    messages = ChatMessageSerializer(many=True)
    context = serializers.CharField()
    openai_api_key = serializers.CharField()
