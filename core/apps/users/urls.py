from typing import Any, Callable, List, Optional, Union
from django.urls import path
from apps.users.views import UserCreateViewSet, UserLoginViewSet, UserLogoutViewSet
# Create your views here.

urlpatterns: List[Union[str, Callable[..., Any], Optional[str]]] = [
    path('create/', UserCreateViewSet.as_view({'post': 'create'}), name='create'),
    path('login/', UserLoginViewSet.as_view({'post': 'create'}), name='login'),
    path('logout/', UserLogoutViewSet.as_view({'post': 'post'}), name='logout'),
]