from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать объект только его автору.
    Для остальных пользователей - только чтение.
    """
    def has_permission(self, request, view):
        # Разрешаем GET, HEAD, OPTIONS всем пользователям
        return (request.method in permissions.SAFE_METHODS or 
                request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Проверяем только авторство - пользователь request.user
        # должен совпадать с автором объекта obj.author
        return obj.author == request.user


# Используем встроенный класс вместо создания своего
from rest_framework.permissions import IsAuthenticated
