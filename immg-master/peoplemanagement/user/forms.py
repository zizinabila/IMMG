from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from master.models import Province, City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def __init__(self   , *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('username', css_class='form-group col-md-12 mb-0')
            ),
            Row(
                Column('email', css_class='form-group col-md-12 mb-0')
            ),
            Row(
                Column('password1', css_class='form-group col-md-12 mb-0')
            ),Row(
                Column('password2', css_class='form-group col-md-12 mb-0')
            ),
            HTML('<div class="form-group">'),
            HTML('<button class="btn btn-primary btn-user btn-block" type="submit">Register Account</button>'),
            HTML('</div>')
        )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

class ProfileUpdateForm(forms.ModelForm):
    def __init__(self   , *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['class'] = 'datepicker'
        self.fields['province'].queryset = Province.objects.none()
        self.fields['city'].queryset = City.objects.none()
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                
                self.fields['province'].queryset = Province.objects.filter(country_id=country_id).order_by('province_desc')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Province queryset
        elif self.instance.country != None:
            self.fields['province'].queryset = self.instance.country.province_set.order_by('province_desc')
        else:
            pass

        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['city'].queryset = City.objects.filter(province_id=province_id).order_by('city_desc')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.province != None:
            self.fields['city'].queryset = self.instance.province.city_set.order_by('city_desc')
        else:
            pass
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('phone_number', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('ktp_address', css_class='form-group col-md-6 mb-0'),
                Column('current_address', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<legend class="border-bottom">Date of Birth</legend>'),
            Row(
                Column('country', css_class='form-group col-md-4 mb-0'),
                Column('province', css_class='form-group col-md-4 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_date', css_class='form-group col-md-4 mb-0'),
                Column('tribe', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML('<legend class="border-bottom">Education</legend>'),
            Row(
                Column('major', css_class='form-group col-md-6 mb-0'),
                Column('class_of', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<legend class="border-bottom">Profile Picture</legend>'),
            'image',
            HTML('<div class="form-group">'),
            HTML('<button class="btn btn-primary btn-user" type="submit">Update</button>'),
            HTML('</div>')
        )

    class Meta:
        model = Profile
        fields = [
            'country',
            'province',
            'city',
            'tribe',
            'gender',
            'phone_number',
            'ktp_address',
            'current_address',
            'major',
            'class_of',
            'birth_date',
            'image'
            ]
        # labels = {
        # 'country': 'country of birth'
        # }