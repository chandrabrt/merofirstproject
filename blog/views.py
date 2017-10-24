from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import ContactForm, CommentForm, AdminForm
from django.core.mail import send_mail, BadHeaderError
from .models import Post
# from django.contrib.auth.decorators import login_required

"""def blog_index(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/index.html', {'all_posts': all_posts})"""


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'all_posts'
    paginate_by = 6
    template_name = 'blog/index.html'


"""def blog_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {
            'post': post,
        })"""


def blog_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()
        return render(request, 'blog/post.html', {
            'post': post,
            'form': form,
        })


"""def adminform(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog:blog_index')
    else:
        form = AdminForm(instance=post)
    return render(request, 'blog/adminform.html', {'form': form})"""


class Adminform(CreateView):
    model = Post
    fields = ['p_language', 'title', 'slug', 'content', 'description', 'image', 'author']
    template_name = 'blog/adminform.html'


class MyUpdateView(UpdateView):
    model = Post
    form_class = AdminForm
    template_name = 'blog/update_task.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # def get_success_url(self):
        #
    # return reverse('blog:blog_index')


def blog_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['chandra2khadka4@gmail.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            sent = True
            #return HttpResponse('Success! Thank you for your message.')
        else:
            sent = False
            # return HttpResponse('Please enter email valid address|all fields require!')
    else:
        sent = False
        form = ContactForm()
    return render(request, "blog/contact.html", {'form': form, 'sent': sent})


def about(request):
    return render(request, 'blog/about.html')


def nav(request):
    return render(request, 'blog/col.html')

