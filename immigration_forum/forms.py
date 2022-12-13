from django import forms
from immigration_forum.models import Post, Country, Comment


class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    header_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'country', 'header_image']


class EditPostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    header_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'country', 'header_image']


class AddCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ['body']