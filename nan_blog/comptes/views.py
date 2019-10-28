import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import *








def register(request):
    return render(request, 'pages/comptes/register.html')


def registerApi(request):

    if request.method == 'POST' :
        
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        image = request.FILES['file']
        # image = request.FILES.get('file')
        print('vvgsgsgsggs',image)
        is_email=False            
        
        if firstname != None and lastname != None and username != None :

            try:
                validate_email(email)
                is_email=True
            except:
                data = {
                    'success':False,
                    'message':'Email is not valide'
                }

            if is_email :
                
                try:

                    user_dup = User.objects.filter(email=email)
                    if user_dup.exists():
                    
                        data={
                            'success':False,
                            'message': 'Ce mail existe Deja dans la BD'
                        }

                    elif password == password2:
                        user = User(username = username, first_name = firstname, last_name = lastname, email = email)
                        user.save()
                        user.profile.imageprofile = image
                        print(user.profile.imageprofile)
                        user.save()
                        # print("UUUUUUU", user.save())
                        user.password = password
                        user.set_password(user.password)
                        user.save()

                        data={
                            'success':True,
                            'message': 'Enregistrement effectue avec succes'
                        }

                    else:
                        data={
                            'success':False,
                            'message':'Mot de passe ne sont pas meme'
                        }

                except:

                    data={
                        'success':False,
                        'message':'Verifier les Champs'
                    }
                    
    else:
        data={
            'success':False,
            'message':'Tous les Champs sont Vides'
        }
    
    return JsonResponse(data, safe=False)



def login_visiteur(request):
    return render(request, 'pages/comptes/login.html')


def loginsApi(request):

    # username = request.POST.get('username')
    # password = request.POST.get('password')

    # print('AAAAAAAAAAAAAA', username)
    # print('AAAAAAAAAAAAAA', password)


    # next = request.GET.get('next', False)
    # user = authenticate(username=username, password=password)
    
    # print(user)

    # if user is not None and user.is_active:
        
    #     # print("user is login")
            
    #     login(request, user)

    #     if next: 
    #         return redirect(next)
    #     else:
    #         data={
    #             'success':True,
    #             'message':'Vous etes connecte'
    #         }
                
    # return JsonResponse(data, safe=False)



    postdata = json.loads(request.body.decode('utf-8'))
    username=postdata['username']
    password=postdata['password']
    print("###################user", username) 
    print("###################user", password) 
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        print("###################user is login")   
        login(request, user)

        data={
            'success':True,
            'message':'connecte'
        }
        # page si connect
    else:
        data={
            'success':False,
            'message':'Erro Login...'
        }
    return JsonResponse(data, safe=False)


def logout_view(request):
    logout(request)
    return redirect('blog:home')



def modif_profil(request):

    data={}
    return render(request, 'pages/comptes/modif_profil.html',data)






