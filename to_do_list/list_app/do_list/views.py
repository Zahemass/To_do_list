from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from . import models
from .models import to_do_list,name_list
from django.views.generic import ListView,View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# If Login The Page Will Show
class index(LoginRequiredMixin,View):
    def get(self,request):
        all_info = to_do_list.objects.filter( user_names_list = request.user,)
        context = {'all_info': all_info,}
        return render(request,"list/index.html",context = context)
    
    def post(self,request):
        all_info = to_do_list.objects.filter( user_names_list = request.user,)
        context = {'all_info': all_info,}
        checked = request.POST.getlist('checked')
        add = request.POST.get('Add')
        delete = request.POST.get('delete')
        print("Successfully running")
        
        #This If block Execute Delete From DataBase
        if delete != None:
            if checked != []:
                    print('You Deselected',checked)
                    for i in checked:
                        for x in models.to_do_list.objects.all():
                            if i == str(x):
                                    x.delete()
                                    print("You successfully deleted")
                                    
            return render(request,"list/index.html",context = context)
        
        #This ElIf block Execute Add From DataBase
        elif add != None: 
                user_list_add = request.POST['add_list']
                names = models.to_do_list(user_list = user_list_add)
                user_id = User.objects.all()
                name_list_loop = models.name_list.objects.all()
                names.save()
                if user_list_add != '':
                    for i in name_list_loop:
                        for x in user_id:
                            if str(i.username == x.username):
                                print(user_list_add)
                                data = to_do_list(user_names_list = request.user,user_list = user_list_add)
                                data.save()
                                break
                        break
                    
                return redirect(reverse('app_list:index'))
            
#This is LoginPage CodeSector    
def loginPage(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        models.name_list.objects.create(username = username)
        if user is not None:
            login(request,user)
            
            return redirect('app_list:index')

        else:
            return HttpResponse("Your Password or username is incorrect!")
    return render(request,"list/login.html")


#This is Signup Page CodeSector 
def signup(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('pass1')
        password_2 = request.POST.get('pass2')
        if password_1 != password_2:
            return HttpResponse("Your Password and Confirm Password Not Same!")
        else:
            my_user = User.objects.create_user(username,email,password_1)
            my_user.save()
            return redirect(reverse('app_list:login'))
    return render(request,"list/signup.html")

#This is Logout Page CodeSector 
def LogoutPage(request):
    logout(request)
    models.name_list.objects.all().delete()
    return redirect('app_list:login')        


    

     
    
        
    






        