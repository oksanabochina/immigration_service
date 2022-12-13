from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from immigration_forum.models import UserProfile, ConsultantProfile, Post
from members.forms import SignUpFrom, EditSettingsForm, PasswordChangeNewForm, CreateUserProfileForm, \
    CreateConsultantProfileForm, UpdateUserProfileForm, UpdateConsultantProfileForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangeView(BasePasswordChangeView):
    form_class = PasswordChangeNewForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


def choose_profile(request):
    return render(request, 'registration/choose_profile.html', {})


class CreateUserProfileView(generic.CreateView):
    form_class = CreateUserProfileForm
    model = UserProfile
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('show_user_profile', kwargs={'pk': self.request.user.userprofile.pk})


class CreateConsultantProfileView(generic.CreateView):
    form_class = CreateConsultantProfileForm
    model = ConsultantProfile
    template_name = 'registration/create_consultant_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('show_consultant_profile', kwargs={'pk': self.request.user.consultantprofile.pk})


class ShowUserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/show_user_profile.html'


class ShowConsultantProfileView(generic.DetailView):
    model = ConsultantProfile
    template_name = 'registration/show_consultant_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowConsultantProfileView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(author=self.kwargs['pk'])
        return context


class UpdateUserProfileView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/update_user_profile.html'
    form_class = UpdateUserProfileForm

    def get_success_url(self, **kwargs):
        return reverse('show_user_profile', kwargs={'pk': self.request.user.userprofile.pk})


class UpdateConsultantProfileView(generic.UpdateView):
    model = ConsultantProfile
    template_name = 'registration/update_consultant_profile.html'
    form_class = UpdateConsultantProfileForm

    def get_success_url(self, **kwargs):
        return reverse('show_consultant_profile', kwargs={'pk': self.request.user.consultantprofile.pk})
