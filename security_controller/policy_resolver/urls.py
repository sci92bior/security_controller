from django.urls import path

from security_controller.policy_resolver.views import add_policy

urlpatterns = [
    path('add/', add_policy, name='add_policy'),
   ]