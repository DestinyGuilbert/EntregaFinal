from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LikePostView, UnlikePostView, ComentarioCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # lista de posts en /pages/
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('crear/', PostCreateView.as_view(), name='post-crear'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='post-editar'),
    path('<int:pk>/borrar/', PostDeleteView.as_view(), name='post-borrar'),
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
    path('<int:pk>/comentar/', ComentarioCreateView.as_view(), name='comentario-crear'),
    
]
