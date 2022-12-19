from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user and request.user.consultantprofile and obj.author == request.user.consultantprofile

        # elif request.user.consultantprofile:
        #     return (request.user and
        #             request.user.consultantprofile and
        #             obj.author == request.user.consultantprofile)

        # elif request.user.consultantprofile:
        #     return obj.author == request.user.consultantprofile
        # else:
        #     return False #нужно ли?


