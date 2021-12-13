import json
from django.http import JsonResponse
from django.views import View
from owners.models import Owners, Dogs

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        age = data['age']
        Owners.objects.create(name=name, email=email, age=age)
        return JsonResponse({'message':'created new owner'}, status=201)    

    def get(self, request):
        owners = Owners.objects.all()
        owners_list = []
        for owner in owners:
            owners_list.append({'name':owner.name, 'email':owner.email, 'age':owner.age})
        dogs = Dogs.objects.all()
        dogs_list = []
        for dog in dogs:
            dogs_list.append({'name': dog.name, 'age':dog.age})
        return JsonResponse({'results_owners':owners_list, 'resulte_dogs':dogs_list}, status=200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = data['owner']
        owner = Owners.objects.get(name=owner)
        name = data['name']
        age = data['age']
        Dogs.objects.create(owner=owner, name=name, age=age)
        return JsonResponse({'message':'created new dog'}, status=201)

    def get(self, request):
        dogs = Dogs.objects.all()
        dogs_list = []
        for dog in dogs:
            dogs_list.append({'owner_id':dog.owner_id, 'name': dog.name, 'age':dog.age})
        return JsonResponse({'results':dogs_list}, status=200)
