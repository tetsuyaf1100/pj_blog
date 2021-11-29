# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

# 編集対象にするフィールド
class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

class Delete(DeleteView):
    model = Post
    success_url = "/"
