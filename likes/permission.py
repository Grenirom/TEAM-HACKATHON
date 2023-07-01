# from rest_framework import permissions
#
#
# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         print(obj, '!!!!!!!!!!!!!!!!')
#         return request.user == obj.user
#

# class IsOwnerOrAdminOrAuthenticated(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request