from portable_npc_backend.chat import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chat', views.ChatCompletionViewSet, basename='chat')
