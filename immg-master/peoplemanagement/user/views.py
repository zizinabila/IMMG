from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from master.models import Province, City

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('user//user_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, f'We have sent you an email, please confirm your email address to complete registration')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user//register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'user//user_active_complete.html')
    else:
        return render(request, 'user//user_active_invalid.html')

def load_province(request):
    country_id = request.GET.get('country')
    if country_id == '':
        country_id = 0
    provinces = Province.objects.filter(country=country_id).order_by('province_desc')
    return render(request, 'master/provinces_ddl.html', {'provinces': provinces})

def load_city(request):
    province_id = request.GET.get('province')
    if province_id == '':
        province_id = 0
    cities = City.objects.filter(province=province_id).order_by('city_desc')
    return render(request, 'master/cities_ddl.html', {'cities': cities})