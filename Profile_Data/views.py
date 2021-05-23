from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from .models import Profile

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        profiles = Profile.objects.filter(full_name=search_input)
    else:
        profiles =Profile.objects.all()
        search_input = ''
    return render(request, 'index.html', {'profiles':profiles, 'search_input': search_input})

def Crate(request):
    if request.method == 'POST':
        new_profile = Profile(
            full_name = request.POST["fullname"],
            phone_number = request.POST["phone-number"],
            address = request.POST["address"],
            Email = request.POST["email"],
        )
        new_profile.save()
        return redirect('/')
    return render(request, 'new.html')

def Profile_ID(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'profile.html', {'profile':profile})

def Edit(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.full_name = request.POST["fullname"]
        profile.phone_number = request.POST["phone-number"]
        profile.address = request.POST["address"]
        profile.Email = request.POST["e-mail"]
        profile.save()
        return redirect('/profile/'+str(profile.id))
    return render(request, 'edit.html', {'profile':profile})

def Delete(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('/')
    return render(request, 'delete.html', {'profile':profile} )

def json(request):
    data = list(Profile.objects.values())
    return JsonResponse(data, safe=False)