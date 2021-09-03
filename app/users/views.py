from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def hello(request):

    if request.method == "POST":

        data = request.POST
        user = User.objects.create(
            email="test@yopmail.com"
        )
        user.set_password(data.get('password'))
        user.save()
        return JsonResponse({"details":"Created Successfully"})
    
    if request.method == "GET":

        user = User.objects.all()
        print(user)
        data = []
        for users in user:
            data.append({
                'email':users.email,
                'password':users.password
            })
        return JsonResponse(data, safe=False)

