
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.core.mail import send_mail
from django.http import HttpResponse


def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            surname = form.cleaned_data['surname']
            address = form.cleaned_data['address']
            fincode = form.cleaned_data['fincode']
            register_type = form.cleaned_data['register_type']
            phone = form.cleaned_data['phone']
            desc = form.cleaned_data['desc']
            attachment = form.cleaned_data['attachment']
            content = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(name,surname,address,fincode,register_type,phone,email,desc,attachment)
            subject = 'New User'
            from_email = 'elchinsalahzada@yandex.com'  # Update with your email address
            send_mail(subject, content, from_email, ['soff3215@gmail.com'])
            form.save()
            return render(request, 'success.html', {'form': form})  
    else:
        form = UserProfileForm()
    return render(request, 'user_profile.html', {'form': form})
