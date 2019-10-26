from django.shortcuts import render

# Create your views here.
def home(request):
    
    data={}
    return render(request, 'pages/blog/index.html',data)

def detail(request , id):
    
    data={}
    return render(request, 'pages/blog/blog-detail.html',data)

def category(request):
    
    data={}
    return render(request, 'pages/blog/category.html',data)

def archive(request):
    
    data={}
    return render(request, 'pages/blog/archive.html',data)

def element(request):
    
    data={}
    return render(request, 'pages/blog/element.html',data)


def senduserimage(request , id):
    # print(id)
    # # postdata = json.loads(request.body.decode('utf-8'))
    # isemail=False
   
    # img = request.FILES.get('file')
    # username = request.POST.get('username')
    # message = request.POST.get('message')
    # email = request.POST.get('email')
    # website = request.POST.get('website')
    # article = Article.objects.get(pk=id)
    # print(article)
    # print("nom ++++++++++++++++++++",message)
    
    # print("img +++++++++++++++++++",img)
    # print("website +++++++++++++++++++",website)
   
    # print("contenu +++++++++++++++++++",message)
    # print("email +++++++++++++++++++",email)
    # if ((username is not None) and (website is not None) and (message is not None) and (img is not None) and (email is not None)):
    #     try:
    #         validate_email(email)
    #         isemail=True
    #     except:
    #         data={
    #             'success':False,
    #             'message':'Entrez un Email Valide...'
    #         }
    #     if isemail:
    #         try:
    #             myimg = Commentaire(username=username, image=img,   contenu=message,  email=email, website=website, article_id=article)
    #             myimg.save()
    #             data={
    #                 'success':True,
    #                 'message':'Vous avez commenter l\'article : {}'.format(article.titre)
    #             }
    #         except Exception as err:
    #             print(err)
    #             data={
    #                 'success':False,
    #                 'message':'Error lor de l\'enregistrement '
    #             }
    # else:
    data={
            # 'success':False,
            # 'message':'Tous Les champs sont requis *',
    }

   
    return JsonResponse(data, safe=False)
def sendreply(request , id):
    # print(id)
    # # postdata = json.loads(request.body.decode('utf-8'))
    # isemail=False
   
    # img = request.FILES.get('file')
    # username = request.POST.get('username')
    # message = request.POST.get('message')
    # email = request.POST.get('email')
    # website = request.POST.get('website')
    # article = Article.objects.get(pk=id)
    # print(article)
    # print("nom ++++++++++++++++++++",message)
    
    # print("img +++++++++++++++++++",img)
    # print("website +++++++++++++++++++",website)
   
    # print("contenu +++++++++++++++++++",message)
    # print("email +++++++++++++++++++",email)
    # if ((username is not None) and (website is not None) and (message is not None) and (img is not None) and (email is not None)):
    #     try:
    #         validate_email(email)
    #         isemail=True
    #     except:
    #         data={
    #             'success':False,
    #             'message':'Entrez un Email Valide...'
    #         }
    #     if isemail:
    #         try:
    #             myimg = Commentaire(username=username, image=img,   contenu=message,  email=email, website=website, article_id=article)
    #             myimg.save()
    #             data={
    #                 'success':True,
    #                 'message':'Vous avez commenter l\'article : {}'.format(article.titre)
    #             }
    #         except Exception as err:
    #             print(err)
    #             data={
    #                 'success':False,
    #                 'message':'Error lor de l\'enregistrement '
    #             }
    # else:
    data={
            # 'success':False,
            # 'message':'Tous Les champs sont requis *',
    }

   
    return JsonResponse(data, safe=False)