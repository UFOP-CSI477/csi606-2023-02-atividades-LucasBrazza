from rest_framework import permissions

class IsOwnerOrSysManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário é o próprio usuário ou se é um sys_manager
        return obj == request.user or (request.user.type == 'sys_manager')

class IsPassengerOrDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário é passengere ou motorista
        return request.user.type in ['passenger', 'driver']

class IsDriverOrSysManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário é motorista ou gerente do sistema
        return request.user.type in ['driver', 'sys_manager']

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário não está autenticado
        return not request.user.is_authenticated