from rest_framework import serializers
from whisper.tokenizer import LANGUAGES

from portable_npc_backend.chat.models import ChatCharacter


class ChatMessageSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=["function", "system", "user", "assistant"])
    content = serializers.CharField()


class ChatCompletionSerializer(serializers.Serializer):
    messages = ChatMessageSerializer(many=True)
    name = serializers.CharField()
    context = serializers.CharField()
    openai_api_key = serializers.CharField()


class ChatCharacterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = ChatCharacter
        fields = ("id", "name", "description", "image")


class TranscribeSerializer(serializers.Serializer):
    audio = serializers.FileField()
    language = serializers.ChoiceField(choices=list(LANGUAGES.values()))
