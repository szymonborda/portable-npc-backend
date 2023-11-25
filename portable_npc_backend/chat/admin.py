from django.contrib import admin

from portable_npc_backend.chat.models import ChatCharacter

class ChatCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "user")

admin.site.register(ChatCharacter, ChatCharacterAdmin)
