from django import forms
from blog.models import Post, Comment


class AdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['p_language', 'title', 'slug', 'content', 'description', 'image',  'author']
        # or
        #fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder':'Write Your messages!!'}))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['name', 'email','comment']



