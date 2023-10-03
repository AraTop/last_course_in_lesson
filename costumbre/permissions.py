from django.shortcuts import render

class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return render(request, 'costumbre/access_denied.html')
        return super().dispatch(request, *args, **kwargs)
