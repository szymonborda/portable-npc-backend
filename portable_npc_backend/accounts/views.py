from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from portable_npc_backend.accounts.serializers import (
    AccountDeleteSerializer,
    AccountRegisterSerializer,
    AccountSerializer,
    ChangePasswordSerializer,
)


class AccountView(viewsets.ViewSet):
    @action(methods=["get"], detail=False, url_name="read")
    def account(self, request, *args, **kwargs):
        data = AccountSerializer(request.user, context={"request": request}).data
        return Response(data)

    @account.mapping.delete
    def delete(self, request, *args, **kwargs):
        AccountDeleteSerializer(instance=request.user).save()
        return Response(status=status.HTTP_200_OK)


class AccountRegisterView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = AccountRegisterSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = AccountRegisterSerializer(user, context={"request": request}).data
        return Response(data, status=status.HTTP_201_CREATED)


class ChangePasswordView(viewsets.ViewSet):
    @action(methods=["put"], detail=False, url_name="update")
    def password(self, request, *args, **kwargs):
        instance = request.user
        serializer = ChangePasswordSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance_serializer = AccountSerializer(instance, context={"request": request})
        return Response(instance_serializer.data)
