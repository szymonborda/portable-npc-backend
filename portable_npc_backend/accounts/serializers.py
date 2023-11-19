from portable_npc_backend.accounts.models import Account
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
        ]


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            is_active=True,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
