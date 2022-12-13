from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, EditPostForm, AddCommentForm
from .models import Country, Post, Comment


class HomeView(ListView):
    model = Country
    template_name = 'home.html'


class CountryView(DetailView):
    model = Country
    template_name = 'country_details.html'

    def get_context_data(self, **kwargs):
        context = super(CountryView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(country=self.kwargs['pk'])
        return context


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user.consultantprofile
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'


class ShowPostView(DetailView):
    model = Post
    template_name = 'show_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowPostView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        is_liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            is_liked = True

        total_likes = post.total_likes()
        context['total_likes'] = total_likes
        context['is_liked'] = is_liked
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = AddCommentForm
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('show_post', kwargs={'pk': self.object.post_id})


def like_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('show_post', args=[str(pk)]))
