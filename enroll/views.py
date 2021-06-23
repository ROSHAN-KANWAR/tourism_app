from django.shortcuts import render,redirect
from .models import District,Allpost,Gallerypost,Contact
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from .filters import Filterpost,Filtergallery
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .form import Templeform,Templeaddphotos,Galleryform
##Home page view
def Home_view(request):
    dis=District.objects.all()
    return render(request, 'home_page.html', {'dis':dis})



##About_page_view

def About_view(request):
    return render(request, 'About_page.html')



def Filters(request):
    all=Allpost.objects.all()
    filter=Filterpost(request.GET,queryset=all)
    all=filter.qs
    return render(request,'Temple_page.html',{'all':all,'filter':filter})




def Templedetail_view(request,id):
    all=Allpost.objects.get(id=id)
    allview=Allpost.objects.order_by('id').reverse()[0:4]
    return render(request, 'TempleView.html',{'all':all,'allview':allview})





##gallery
def Filtersgallery(request):
    gls=Gallerypost.objects.all()
    filter=Filtergallery(request.GET,queryset=gls)
    gls=filter.qs
    return render(request,'Gallery_page.html',{'gls':gls,'filter':filter})


def Gallery_imageview(request,id):
    gls=Gallerypost.objects.get(id=id)
    allview = Gallerypost.objects.order_by('id').reverse()[0:6]
    all = Allpost.objects.order_by('id').reverse()[0:6]
    return render(request, 'Gallery_imageview.html',{'gls':gls,'allview':allview,'all':all})



##contact_page_view

def Contact_view(request):
    if request.method =="POST":
       name=request.POST['name']
       email = request.POST['email']
       problem = request.POST['problem']
       user=Contact(name=name,email=email,problem=problem)
       user.save()
       # send_mail('Contact Forms',
       # "If any query please mail..." ,
       # settings.EMAIL_HOST_USER,
       #  [email],
       # fail_silently=False)
       subject = 'Real Contact Form'
       to = email
       #   res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
       html_tem = 'cgtour.html'
       html_mes = render_to_string(html_tem)
       message = EmailMessage(subject, html_mes, settings.EMAIL_HOST_USER, [to])
       message.content_subtype = 'html'
       message.send()
       return redirect('home')

    return render(request, 'Contact_page.html')
##login_admin


def Admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            return redirect('admin_login')

        user = authenticate(request, username=username, password=request.POST['password'])
        # if user is not None:
        #     login(request,user)
        #     messages.info(request, 'Login Successfully ! Now enjoy app ')
        #     return redirect('/')
        if user is None:
            return redirect('admin_login')
        login(request, user)
        return redirect('dash')
    return render(request,'logins_admin.html')

##logout
def Admin_logout(request):
    logout(request)
    return redirect('home')
##dashboard
@login_required(login_url='home')
def dashboard(request):
    temple=Allpost.objects.all().reverse()[0::-1]
    gls=Gallerypost.objects.all().reverse()[0::-1]
    return render(request,'dashboard.html',{'tem':temple,'gls':gls})



#temple post delete
def delete_data(request,id):
    if request.method=='POST':
        pi=Allpost.objects.get(pk=id)
        pi.delete()
    return render(request,'del.html',{'id':id})

#gallery post delete
def delete_data_gl(request,id):
    if request.method=='POST':
        pi=Gallerypost.objects.get(pk=id)
        pi.delete()
    return render(request,'del1.html',{'id':id})

##temple post_edit
def edit_data(request,id):
 try:
      if request.method == "POST":
        fm = Allpost.objects.get(id=id)
        pos=request.POST or None
        fil=request.FILES or None
        form = Templeform(pos,fil, instance=fm)
        if form.is_valid():
            form.save()
            return redirect("dash")
        else:
           fm=Allpost.objects.get(id=id)
           fm=Templeform(instance=fm)
        return render(request, 'edit.html', {'fm':fm})
 except Exception as e:
     return redirect("home")

#gallery edit
def edit_data_gl(request,id):
 try:
      if request.method == "POST":
        fm = Gallerypost.objects.get(id=id)
        pos=request.POST or None
        fil=request.FILES or None
        form = Galleryform(pos,fil, instance=fm)
        if form.is_valid():
            form.save()
            return redirect("dash")
        else:
           fm=Gallerypost.objects.get(id=id)
           fm=Galleryform(instance=fm)
        return render(request, 'edit1.html', {'fm':fm})
 except Exception as e:
     return redirect("home")

##temple post add photo
@login_required(login_url='home')
def Templephotoadd(request):
    if request.method=="POST":
        fm=Templeaddphotos(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('dash')
    else:
        fm=Templeaddphotos()
    return render(request,'templeaddphoto.html',{'fm':fm})


##temple post add photo
@login_required(login_url='home')
def Galleryphotoadd(request):
    if request.method=="POST":
        fm=Galleryform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('dash')
    else:
        fm=Galleryform()
    return render(request,'galleryaddphoto.html',{'fm':fm})