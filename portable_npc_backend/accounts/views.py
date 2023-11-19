from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from portable_npc_backend.accounts.serializers import (
    AccountRegisterSerializer,
    AccountSerializer,
)


class AccountView(viewsets.ViewSet):
    @action(methods=["get"], detail=False, url_name="read")
    def account(self, request, *args, **kwargs):
        data = AccountSerializer(request.user, context={"request": request}).data
        return Response(data)


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
