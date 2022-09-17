from django.shortcuts import render
from django.views import View
from .models import Rol
from .models import Employee
from .models import Enterprise
from .models import Profile
from .models import Transaction
from django.http.response import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class ProfileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            pro=list(Profile.objects.filter(id_profile=id).values())
            if (len(pro)>0):
                ProResponse=pro[0]
                data={"Response ->":ProResponse}
            else:
                data={"Response ->": "Object not found"}
        else:
            pro=list(Profile.objects.values())
            data={"Response ->":pro}
        return JsonResponse(data)

    def post(self, request):
        data=json.loads(request.body)
        Profile.objects.create(id_profile=data["id_profile"],image=data["image"],phone=data["phone"],
                               user=data["user"],createdAT=data["createdAT"],updateAT=data["updateAT"])
        return JsonResponse(data)

    def put(self, request, id):
        data=json.loads(request.body)
        pro=list(Profile.objects.filter(id_profile=id).values())
        if (len(pro)>0):
            prof=Profile.objects.get(id_profile=id)
            prof.image=data['image']
            prof.phone = data['phone']
            prof.user = data['user']
            prof.createdAT = data['createdAT']
            prof.updateAT = data['updateAT']
            prof.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)

    def delete(self,request,id):
        pro=list(Profile.objects.filter(id_profile=id).values())
        if(len(pro)>0):
            Profile.objects.filter(id_profile=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not delete Successfully.."}
        return JsonResponse(message)


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


class EmployeeViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): #Read
        if (id > 0):
            employee=list(Employee.objects.filter(id_employee=id).values())
            if (len(employee)>0):
                employeeResponse=employee[0]
                data={'employee ->':employeeResponse}
            else:
                data={'message': "Object not found"}
        else:
            employee=list(Employee.objects.values())
            data={'employee':employee}       
        return JsonResponse(data)         

    def post(self, request): #Create
        data=json.loads(request.body)
        Employee.objects.create(id_employee=data["id_employee"],email=data["email"])
        return JsonResponse(data)

    def put(self, request, id): #Update
        data=json.loads(request.body)
        employee=list(Employee.objects.filter(id_employee=id).values())
        if (len(employee)>0):
            employees=Employee.objects.get(id_employee=id)
            employees.email=data['email']
            employees.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)    

    def delete(self,request,id): #Delete
        employee=list(Employee.objects.filter(id_employee=id).values())
        if(len(employee)>0):
            Employee.objects.filter(id_employee=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not delete Successfully.."}
        return JsonResponse(message)  

class EnterpriseViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            ent=list(Enterprise.objects.filter(id_enterprise=id).values())
            if (len(ent)>0):
                entResponse=ent[0]
                data={'Enterprise ->':entResponse}
            else:
                data={'message': "Object not found"}
        else:
            ent=list(Enterprise.objects.values())
            data={'listEnterprise':ent}       
        return JsonResponse(data)         

    def post(self, request):
        data=json.loads(request.body)
        try:
            pro=Profile.objects.get(id_profile=data["id_profile"])
            transaction = Transaction.objects.get(id_transaction=data["id_transaction"])
            ent=Enterprise.objects.create(id_enterprise=data["id_enterprise"],name=data["name"],document=data["document"],
                                          phone=data["phone"],address=data["address"],id_profile=pro,
                                          id_transaction=transaction,createdAT=data["createdAT"],updateAT=data["updateAT"])
            ent.save()
            message={"Response:":"Updated Successfully.."}
            return JsonResponse(message)
        except Enterprise.DoesNotExist:
            message={"Response:":"Not exist.."} 
        except Enterprise.DoesNotExist:
            message={"Response:":"Not exist.."}
        return JsonResponse(message)

    def put(self, request, id):
        data=json.loads(request.body)
        ent=list(Enterprise.objects.filter(id_enterprise=id).values())
        if (len(ent)>0):
            pro=Profile.objects.get(id_profile=data["id_profile"])
            transaction = Transaction.objects.get(id_transaction=data["id_transaction"])
            enterprise=Enterprise.objects.get(id_enterprise=id)
            enterprise.name=data['name']
            enterprise.document=data['document']
            enterprise.phone=data['phone']
            enterprise.address=data['address']
            pro.id_profile=data['id_profile']
            transaction.id_transaction=data['id_transaction']
            enterprise.createdAT=data['createdAT']
            enterprise.updateAT=data['updateAT']
            enterprise.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)

    def delete(self,request,id):
        ent=list(Enterprise.objects.filter(id_enterprise=id).values())
        if(len(ent)>0):
            Enterprise.objects.filter(id_enterprise=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not exist.."}
        return JsonResponse(message)
