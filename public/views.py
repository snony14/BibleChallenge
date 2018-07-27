from django.shortcuts import render
from django.http import HttpResponse

'''
This contains all website that are public to the users!!
'''

def home(request):
    return render(request, "public/home.html",dict())#HttpResponse("This is home", content_type="text/plain")

def search_team(request):
    #TODO should contain the join button!! but user must have logged in!!
    return HttpResponse("searching all team that are public")

def about(request):
    return HttpResponse("About us!")

#TODO requires validation, now we take it for granted, maybe should move this to public app
def register_user(request):
    error = dict()
    if request.method=='POST':
        #TODO create form later on
        firstname = request.POST.get("firstname", "")
        lastname = request.POST.get("lastname", "")
        email = request.POST.get("email", "")
        psw = request.POST.get("password", "")
        psw_confirm = request.POST.get("password_confirm", "")
        are_token = all(len(tk)>0 for tk in [firstname, lastname, email, psw, psw_confirm])
        #TODO
        psw_equals = psw == psw_confirm
        user_not_exist = not (len(User.objects.filter(email=email)) > 0)
        if psw_equals and user_not_exist:
            user = User.objects.create_user(username=email,first_name= firstname
            ,last_name=lastname
            , email=email
            , password = psw)
            user.save()
            profile = Profile(user=user)
            profile.save()
            return redirect("/login")
        else:
            error["password"] = "Password should match" if not psw_equals else ""
            error["email"] = "email exists" if not user_not_exist else ""
    return render(request, 'user/register.html', error)
