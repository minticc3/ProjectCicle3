from tkinter import E
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
    
    def post(self, request):
        data=json.loads(request.body)
        Profile.objects.create(id_profile=data["id_profile"],image=data["image"],phone=data["phone"],
                               user=data["user"],createdAT=data["createdAT"],updateAT=data["updateAT"])
        return JsonResponse(data)


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

class TransactionViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data=json.loads(request.body)
        try:
            pro=Profile.objects.get(id_profile=data["id_profile"])
            tra=Transaction.objects.create(id_transaction=data["id_transaction"],concept=data["concept"],amount=data["amount"],id_profile=pro,enterprises=data["enterprises"],createdAT=data["createdAT"],updateAT=data["updateAT"])
            tra.save()
            message={"Response:":"Create Successfully.."}
            return JsonResponse(message)
        except Transaction.DoesNotExist:
            message={"Response:":"Not Exists..."}
        except Transaction.DoesNotExist:
            message={"Response:":"Not Exists..."}
        return JsonResponse(message)


    def get(self, request, id=0):
        if (id > 0):
            tran=list(Transaction.objects.filter(id_transaction=id).values())
            if (len(tran)>0):
                TranResponse=tran[0]
                data={"Response ->":TranResponse}
            else:
                data={"Response ->": "Object not found"}
        else:
            tran=list(Transaction.objects.values())
            data={"Response ->":tran}
        return JsonResponse(data)

    
    def put(self, request, id):
        data=json.loads(request.body)
        tran=list(Transaction.objects.filter(id_transaction=id).values())
        if (len(tran)>0):
            pro=Profile.objects.get(id_profile=data["id_profile"])
            tran=Transaction.objects.get(id_transaction=id)
            tran.concept=data['concept']
            tran.amount = data['amount']
            pro.id_profile=data['id_profile']
            tran.enterprises=data['enterprises']
            tran.createdAT = data['createdAT']
            tran.updateAT = data['updateAT']
            tran.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)

    def delete(self,request,id):
        tran=list(Transaction.objects.filter(id_transaction=id).values())
        if(len(tran)>0):
            Transaction.objects.filter(id_transaction=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not delete Successfully.."}
        return JsonResponse(message)


class RolViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
        data=json.loads(request.body)
        Rol.objects.create(id_role=data["id_role"],name_role=data["name_role"])
        return JsonResponse(data)

    
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


    def post(self, request): #Create
        data = json.loads(request.body)
        try:
            pro = Profile.objects.get(id_profile=data["id_profile"])
            rol = Rol.objects.get(id_role=data['id_role'])
            ent = Enterprise.objects.get(id_enterprise=data['id_enterprise'])
            tran = Transaction.objects.get(id_transaction=data['id_transaction'])
            empl = Employee.objects.create(id_employe=data['id_employe'],email=data['email'],password=data['password'],profile=pro,
                                           id_role=rol,id_enterprise=ent,id_transaction=tran,createdAT=data['createdAT'],
                                           updateAT=data['updateAT'])
            empl.save()
            message = {"Response:": "Create Successfully.."}
            return JsonResponse(message)
        except Employee.DoesNotExist:
            message = {"Response:": "Not Exists..."}
        except Employee.DoesNotExist:
            message = {"Response:": "Not Exists..."}
        return JsonResponse(message)

    def get(self, request, id=0): #Read
        if (id > 0):
            employee=list(Employee.objects.filter(id_employe=id).values())
            if (len(employee)>0):
                employeeResponse=employee[0]
                data={'employee ->':employeeResponse}
            else:
                data={'message': "Object not found"}
        else:
            employee=list(Employee.objects.values())
            data={'employee':employee}       
        return JsonResponse(data)         

    
    def put(self, request, id): #Update
        data=json.loads(request.body)
        employee=list(Employee.objects.filter(id_employe=id).values())
        if (len(employee)>0):
            employees=Employee.objects.get(id_employe=id)
            employees.email=data['email']
            employees.password=data['password']
            employees.save()
            message={"Response:":"Updated Successfully.."}
        else:
            message={"Response:":"Not Successfully.."}
        return JsonResponse(message)    

    def delete(self,request,id): #Delete
        employee=list(Employee.objects.filter(id_employe=id).values())
        if(len(employee)>0):
            Employee.objects.filter(id_employe=id).delete()
            message={"Response:":"Delete Successfully.."}
        else:
            message={"Response:":"Not delete Successfully.."}
        return JsonResponse(message)  

class EnterpriseViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data=json.loads(request.body)
        try:
            pro=Profile.objects.get(id_profile=data["id_profile"])
            transaction = Transaction.objects.get(id_transaction=data["id_transaction"])
            ent=Enterprise.objects.create(id_enterprise=data["id_enterprise"],name=data["name"],document=data["document"],
                                          phone=data["phone"],address=data["address"],id_profile=pro,
                                          id_transaction=transaction,createdAT=data["createdAT"],updateAT=data["updateAT"])
            ent.save()
            message={"Response:":"Create Successfully.."}
            return JsonResponse(message)
        except Enterprise.DoesNotExist:
            message={"Response:":"Not exist.."} 
        except Enterprise.DoesNotExist:
            message={"Response:":"Not exist.."}
        return JsonResponse(message)


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

def loginUser(request):
    if(request.method=='POST'):
        try:
            UserValidation = Employee.objects.get(email=request.POST['email'],password=request.POST['password'])
            if(UserValidation.id_role_id==1):
                request.session['email']=UserValidation.email
                print(UserValidation.email, UserValidation.password)
                return  render(request, 'Admin/welcome.html')
            elif(UserValidation.id_role_id==2):
                request.session['email']=UserValidation.email
                return  render(request, 'Employee/welcome.html')
        except Employee.DoesNotExist:
            message.warning(request, "Usuario o Contraseña Incorrectos")
    return render(request, 'login/login.html')

def formRegister(request):
    return render(request, 'Admin/registro.html')

def formUpdate(request,id):
    employee=Employee.objects.get(id_employe=id)
    data={
        'employee':employee
    }
    return render(request,"actualizaremp.html",data)

def updateEmployee(request):
    id_employe = request.POST['id_employe']
    email = request.POST['email']
    password =  request.POST['password']
    profile = request.POST['profile']
    id_role = request.POST['id_role']
    id_enterprise = request.POST['id_enterprise']
    id_transaction = request.POST['id_transaction']
    createdAT = request.POST['createdAT']
    updateAT = request.POST['updateAT']
    emp=Employee.objects.get(id_employe=id_employe)
    emp.id_employee=id_employe    
    emp.email = email
    emp.password = password 
    emp.profile = profile
    emp.id_role = id_role
    emp.id_enterprise = id_enterprise
    emp.id_transaction = id_transaction
    emp.createdAT = createdAT
    emp.updateAT = updateAT