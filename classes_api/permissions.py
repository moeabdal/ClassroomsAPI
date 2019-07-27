from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message = "You do not have permission to do this."

	def has_object_permission(self, request, view, obj):
		if request.user == obj.teacher or reuqest.user.is_staff:
			return True
		else:
			return False