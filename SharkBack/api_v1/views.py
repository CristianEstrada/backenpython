from django.http import HttpResponse, JsonResponse, Http404
from .models import User

def index(request):
    return HttpResponse("Bienvenido! a la api v1")

def getusers(request):
    try:
        user = User.objects.all()
        user_data = {
            'users': [
                {
                    'id': u.id,
                    'username': u.username,
                    'email': u.email,
                    'role': u.role
                } for u in user
            ]
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        raise Http404("No hay usuarios registrados")

def getuserbyid(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        raise Http404("Usuario no encontrado")