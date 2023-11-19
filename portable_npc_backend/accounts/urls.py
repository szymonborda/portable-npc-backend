from portable_npc_backend.accounts import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.AccountView, basename="account")
router.register(r"register", views.AccountRegisterView, basename="account_register")
