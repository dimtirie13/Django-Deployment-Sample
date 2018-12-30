from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
from first_app.forms import NewUserForm,UserProfileInfoForm,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

@login_required
def special(request):
        return HttpResponse('YOU ARE LOGING IN! , NICE')


@login_required
def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def user_login(request):
        if request.method == 'POST':
                # username is what we called it in the html file
                username = request.POST.get('username')
                password = request.POST.get('password')


                # django built in authentication
                user = authenticate(username=username,password=password)

                if user:
                        if user.is_active:
                                login(request,user)
                                #send user somewhere after log in
                                return HttpResponseRedirect(reverse('index'))
                        else:
                                return HttpResponse('ACCOUNT NOT ACTIVE')
                else:
                        print('Someone tried to log in and failed')
                        print(f"Username: {username} and Password: {password}")
                        return HttpResponse("INVALID LOG IN DETAILS")

        else:
             return render(request,'first_app/login.html',{})   

            

def signup_page(request):
        registered = False

        if request.method =="POST":
                user_form = UserForm(data=request.POST)
                profile_form = UserProfileInfoForm(data=request.POST)

                if user_form.is_valid() and profile_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password) #hasing password
                        user.save()

                        profile = profile_form.save(commit=False)
                        profile.user = user #sets up ne to one relationship

                        # can also be used to upload a CSV
                        if 'profile_pic' in request.FILES:
                                profile.profile_pic = request.FILES['profile_pic']

                        profile.save()

                        registered=True
                else:
                        print(user_form.errors,profile_form.errors)
        else:
                user_form= UserForm()
                profile_form = UserProfileInfoForm()

        return render(request,'first_app/signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def other(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'first_app/other.html',context_dict)

def relative(request):
        return render(request,'first_app/relative_url_templates.html')

def users(request):
        form = NewUserForm()

        if request.method == 'POST':
                form = NewUserForm(request.POST)
                # to commit to database
                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                else:
                        print('ERROR FROM INVALID FORM')
        return render(request,'first_app/users.html',{'signup_form':form})

        user_list = User.objects.order_by('first_name')
        user_dict = {'users': user_list}
        return render(request,'first_app/users.html',context=user_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request,'first_app/form_page.html',{'form':form})

# def signup_page(request):
#         sign_up_form = forms.Signup()

#         return render(request,'first_app/signup.html',{'sign_up_form':sign_up_form})