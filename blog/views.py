from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView
#models와 다른 파일이기 때문에 Post 사용하려면 import!!
from blog.models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

# <CBV 스타일로 페이지 만들기>
#블로그 목록
#post_list.html
class PostCreate(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate,self).form_valid(form)
            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')
                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)
            return response
        else:
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView): #모델명_form
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    template_name = 'blog/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, object_list = None, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tag_str_default'] = '; '.join(tags_str_list)
            return context

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear()
        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')
            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)
        return response

class PostList(ListView) :
    model = Post
    ordering = '-pk'
    paginate_by = 5 #화면에 5개씩 출력
#   template_name = 'blog/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#반드시 PostList 다음에 선언, list 내용을 알아야 검색이 가능하기 때문
class PostSearch(PostList):
    paginate_by = None

    #전달받은 검색결과로 포스트를 찾음
    def get_queryset(self):
        q = self.kwargs['q'] #검색결과를 가져옴
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct() #똑같은 포스트가 여러개이면 하나만 가져오겠다
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']  # 검색결과를 가져옴
        context['search_info'] = f'Search : {q}({self.get_queryset().count()})'
        return context

#블로그 상세 페이지
#post_detail.html
class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

#카테고리
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'blog/post_list.html',
                  {
                      'post_list': post_list,
                      'categories': Category.objects.all(),
                      'no_category_post_count': Post.objects.filter(category=None).count(),
                      'category': category
                  }
                  )

#태그
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'blog/post_list.html',
                  {
                      'post_list': post_list,
                      'categories': Category.objects.all(),
                      'no_category_post_count': Post.objects.filter(category=None).count(),
                      'tag': tag
                  }
                  )

#<FBV 스타일로 페이지 만들기>

#index 함수 - template안 html 파일과 연결
#def index(request) :
#   posts = Post.objects.all().order_by('-pk')

#   return render(request, 'blog/post_list.html',
#                 {
#                     #post도 같이 전달
#                     'posts' : posts
#                 })

#single_post_page 함수 - template안 html 파일과 연결
#def single_post_page(request, pk) :
   #특정 페이지만 가지고 옴
#   post = Post.objects.get(pk=pk)

#   return render(request, 'blog/post_detail.html',
#                 {
#                     'post': post
#                 })