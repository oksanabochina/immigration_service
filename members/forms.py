from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from immigration_forum.models import UserProfile, ConsultantProfile, Country


class SignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(SignUpFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PasswordChangeNewForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class CreateUserProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),
                                   required=False)
    website_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    instagram_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    facebook_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)
    twitter_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    linkedin_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic', 'website_url', 'instagram_url',
                  'facebook_url', 'twitter_url', 'linkedin_url']


class CreateConsultantProfileForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),
                                   required=False)
    website_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    instagram_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    facebook_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)
    twitter_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    linkedin_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)

    class Meta:
        model = ConsultantProfile
        fields = ['country', 'bio', 'profile_pic', 'website_url', 'instagram_url',
                  'facebook_url', 'twitter_url', 'linkedin_url']


class UpdateUserProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),
                                   required=False)
    website_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    instagram_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    facebook_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)
    twitter_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    linkedin_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic', 'website_url', 'instagram_url',
                  'facebook_url', 'twitter_url', 'linkedin_url']


class UpdateConsultantProfileForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),
                                   required=False)
    website_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    instagram_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    facebook_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)
    twitter_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    linkedin_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=False)

    class Meta:
        model = ConsultantProfile
        fields = ['country', 'bio', 'profile_pic', 'website_url', 'instagram_url',
                  'facebook_url', 'twitter_url', 'linkedin_url']

