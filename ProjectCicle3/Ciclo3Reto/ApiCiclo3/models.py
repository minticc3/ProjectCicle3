from django.db import models

# Create your models here.
class Profile(models.Model): #Kevin
    id_profile = models.IntegerField(primary_key=True)
    image=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    user=models.CharField(max_length=15)
    createdAT = models.DateField()
    updateAT = models.DateField()

class Transaction(models.Model): #Bibiana
    id_transaction = models.IntegerField(primary_key=True)
    concept = models.CharField(max_length=80)
    amount = models.FloatField(max_length=10)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    enterprises = models.CharField(max_length=30)
    createdAT = models.DateField()
    updateAT = models.DateField()

class Enterprise(models.Model): #Andrea & Keyla
    id_enterprise = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    document = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    createdAT = models.DateField()
    updateAT = models.DateField()

class Rol(models.Model): #Realizado en grupo
    id_role = models.IntegerField(primary_key=True)
    name_role = models.CharField(max_length=10, default="Admin")

class Employee(models.Model): #Leo
    id_employee = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    id_role = models.ForeignKey(Rol, on_delete=models.CASCADE)
    id_enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    id_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    createdAT = models.DateField()
    updateAT = models.DateField()






