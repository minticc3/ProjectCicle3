from django.shortcuts import render
from django.views import View
from .models import Rol
from django.http.response import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class RolViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            rol=list(Rol.objects.filter(id_role=id).values())
            if (len(rol)>0):
                rolResponse=rol[0]
                data={'rol ->':rolResponse}
            else:
                data={'message': "Object not found"}
        else:
            rol=list(Rol.objects.values())
            data={'rol':rol}       
        return JsonResponse(data)         


    def post(self, request):
        data=json.loads(request.body)
        Rol.objects.create(id_role=data["id_role"],name_role=data["name_role"])
        return JsonResponse(data)

    def put(self, request, id):
        data=json.loads(request.body)
        rol=list(Rol.objects.filter(id_role=id).values())
        if (len(rol)>0):
            rols=Rol.objects.get(id_role=id)
            rols.name_role=data['name_role']
            rols.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)    

    def delete(self,request,id):
        rol=list(Rol.objects.filter(id_role=id).values())
        if(len(rol)>0):
            Rol.objects.filter(id_role=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not delete Successfully.."}
        return JsonResponse(message)  


