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


class AccountDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

    def save(self, **kwargs):
        return self.instance.delete()


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = ("old_password", "new_password")

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError("Incorrect old password.")

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
