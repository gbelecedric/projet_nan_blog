from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    
    data={}
    return render(request, 'pages/blog/index.html',data)

def detail(request , titre):
    
    # lien = Link.objects.filter(status=True).order_by('-date_add')
    # image = Background.objects.filter(status=True).order_by('-date_add')
    archive = Categorie.objects.filter(status=True).order_by('-date_add') 
    alltag = Tag.objects.filter(status=True)
    article = Article.objects.filter(titre_slug=titre)[:1].get()
    categorie = Categorie.objects.filter(status=True).order_by('-date_add')
    tag = article.tag_name.all()
    comment = Commentaire.objects.filter(article_id = article).order_by('-date_add')
    comment7 = Commentaire.objects.filter(article_id = article).order_by('-date_add')[5::]

    print(comment7)
    
    data={
        'verif':len(comment7),
        # 'lien':lien,
        # 'image':image,
        'alltag':alltag,
        'archive':archive,
        'tag':tag,
        'categorie':categorie,
        'comment':comment,
        'article':article,
    }
    return render(request, 'pages/blog/blog-detail.html',data)

def categorie(request, titre):
    
    data={
        'titre': titre
    }
    return render(request, 'pages/blog/category.html',data)

def archive(request):
    
    data={}
    return render(request, 'pages/blog/archive.html',data)

def voirplus(request):
    allartiacle = Article.objects.filter(status=True)
    paginator = Paginator(allartiacle, 10)
    page = request.GET.get('page') 

    allartiacle = paginator.get_page(page)
    
    data={
        'allartiacle': allartiacle,
    }
    return render(request, 'pages/blog/voirplus.html',data)

def ajout(request):
    
    data={}
    return render(request, 'pages/dashbord/ajout.html',data)

def element(request):
    
    data={}
    return render(request, 'pages/blog/element.html',data)

def dashbord(request):
    
    data={}
    return render(request, 'pages/dashbord/dashbord.html',data)

def dashpost(request):
    
    data={}
    return render(request, 'pages/dashbord/posts.html',data)

def dashdetail(request):
    
    data={}
    return render(request, 'pages/dashbord/dashdetail.html',data)

def error(request):
    
    data={}
    return render(request, 'pages/dashbord/page_404.html',data)
def modif_profil(request):
    
    data={}
    return render(request, 'pages/blog/modif_profil.html',data)


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