from django.shortcuts import render

#TODO for future work, redirect here!!
# Create your views here.
def login(request):
    return render(request, 'user/dashboard.html', dict())

def logout(request):
    return render(request, 'user/dashboard.html', dict())

def profile(request):
    return render(request, 'user/dashboard.html', dict())

def challenges(request):
    return render(request, "user/challenges.html", dict())

def teams(request):
    #Ability to add team etc.
    return render(request, "user/teams.html", dict())

def settings(request):
    return render(request, "user/settings.html", dict())


'''
Need decorator in order to know login in people and not logging in people!!
'''
