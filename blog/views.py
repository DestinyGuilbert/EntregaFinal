from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
#create
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# views
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import Post, Comentario, Like

# Delete
from django.views.generic.edit import DeleteView


class PostListView(ListView):
    model = Post
    template_name = 'AppCoder/Blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(subtitulo__icontains=query)
            )
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppCoder/Blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comentarios'] = post.comentarios.all().order_by('-fecha')  # ¡esto es clave!
        context['likes_count'] = post.likes.count()

        user = self.request.user
        if user.is_authenticated:
            context['user_liked'] = post.likes.filter(usuario=user).exists()
        else:
            context['user_liked'] = False

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'AppCoder/Blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'AppCoder/Blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor or self.request.user.is_staff
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'AppCoder/Blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor or self.request.user.is_staff

# Create your views here.



@method_decorator(login_required, name='dispatch')
class LikePostView(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        Like.objects.get_or_create(post=post, usuario=request.user)
        return redirect('post-detail', pk=pk)
    
@method_decorator(login_required, name='dispatch')
class UnlikePostView(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        Like.objects.filter(post=post, usuario=request.user).delete()
        return redirect('post-detail', pk=pk)
    

class ComentarioCreateView(CreateView):
    model = Comentario
    fields = ['contenido']
    template_name = 'AppCoder/Blog/comentario_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})