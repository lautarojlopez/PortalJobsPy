from usuarios.models import UserProfile
# Middleware para obtener el tipo de cuenta
class TipoCuenta:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            tipo_cuenta = UserProfile.objects.get(datos_id=request.user.id).tipo_cuenta
            request.tipo_cuenta = tipo_cuenta
        else:
            request.tipo_cuenta = None
        response = self.get_response(request)
        return response

class GetUserProfile:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            userprofile = UserProfile.objects.get(datos_id=request.user.id)
            request.userprofile = userprofile
        else:
            request.userprofile = None
        response = self.get_response(request)
        return response