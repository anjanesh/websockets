## application/routing.py
from django.urls import path
from application.consumers import TerraformUpdates

websocket_urlpatterns = [
    path('test', TerraformUpdates.as_asgi()),    
]