from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User, County


def log_in(request):
    context = {
        'error_message': None
    }
    return render(request, 'counties/login.html', context)


def sing_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('counties:index')
    else:
        context = {
            'error_message': 'Nume sau parola incorectă!'
        }
        return render(request, 'counties/login.html', context)


def log_out(request):
    logout(request)
    context = {
        'error_message': "Ai fost scos afară!"
    }
    return render(request, 'counties/login.html', context)


def index(request):
    user_state = request.user.is_authenticated

    # The logic for the gathering of unsupervised counties.
    unsupervised_counties = []
    for unsupervised_county in County.objects.all():
        if unsupervised_county.admins.count() == 0:
            unsupervised_counties.append(unsupervised_county.county_name)
        else:
            admins = unsupervised_county.admins.count()
            for admin in unsupervised_county.admins.all():
                if admin.state != "activ":
                    admins -= 1
            if admins == 0:
                unsupervised_counties.append(unsupervised_county.county_name)

    context = {
        'user_state': user_state,
        'unsupervised_counties': unsupervised_counties,
    }
    return render(request, 'counties/index.html', context)


def county(request, county_name):
    user_state = request.user.is_authenticated
    current_user = request.user
    main_admins = User.objects.filter(state="activ", main_county=county_name)
    admin_list = User.objects.filter(state="activ", county__county_name=county_name).order_by('last_name')
    county_name = get_object_or_404(County, county_name=county_name).county_name
    context = {
        'user_state': user_state,
        'county_name': county_name,
        'main_admins': main_admins,
        'admin_list': admin_list,
        'current_user': current_user
    }
    return render(request, 'counties/county.html', context)


def edit(request, last_name, first_name):
    if request.user.first_name == first_name and request.user.last_name == last_name:
        admin = get_object_or_404(User, last_name=last_name, first_name=first_name)
        county_list = County.objects.all().order_by('county_name')
        context = {
            'admin': admin,
            'county_list': county_list
        }
        return render(request, 'counties/edit.html', context)
    else:
        context = {
            'error_message': "Nu ai permisiune să editezi acest utilizator!"
        }
        return render(request, 'counties/login.html', context)


def change(request, last_name, first_name):
    if request.user.last_name == last_name and request.user.first_name == first_name:
        admin = get_object_or_404(User, last_name=last_name, first_name=first_name)
        all_counties = County.objects.all().order_by('county_name')
        selected_counties = request.POST.getlist('county')
        selected_state = request.POST['state']
        new_phone = request.POST['phone']
        if len(new_phone) == 0:
            new_phone = "None"
        new_email = request.POST['email']
        if len(new_email) == 0:
            new_email = "None"
        admin.state = selected_state
        admin.phone = new_phone
        admin.email = new_email
        admin.save()
        admin.county_set.clear()
        for selected_county in all_counties:
            if selected_county.county_name in selected_counties:
                selected_county.admins.add(admin)
        return redirect('counties:index')
    else:
        context = {
            'error_message': "Nu ai permisiune să editezi acest utilizator!"
        }
        return render(request, 'counties/login.html', context)


def all_admins(request):
    user_state = request.user.is_authenticated
    current_user = request.user
    admin_list = User.objects.all().order_by('last_name')
    context = {
        'user_state': user_state,
        'admin_list': admin_list,
        'current_user': current_user
    }
    return render(request, 'counties/all_admins.html', context)
