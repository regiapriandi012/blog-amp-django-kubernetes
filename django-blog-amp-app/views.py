from django.shortcuts import render
from django.views import generic
from .models import Post, Photography, Award, Certification, Project, Publication, Programing, Comment
from django.http import HttpResponse
from django.views import View
from .forms import CommentForm, CommentFormAmp
from django.shortcuts import render, get_object_or_404

class PostListAmp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-amp.html'
    paginate_by = 3

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-regular.html'
    paginate_by = 3

# class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'blog_detail.html'

def post_detail_amp(request, slug):
    template_name = 'blog-detail-amp.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentFormAmp(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentFormAmp()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def post_detail(request, slug):
    template_name = 'blog-detail-regular.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = Comment()
            new_comment.name = comment_form.cleaned_data['name']
            new_comment.email = comment_form.cleaned_data['email']
            new_comment.body = comment_form.cleaned_data['body']
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class AdsView(View):
    def get(self, request, *args, **kwargs):
        line = "google.com, pub-7279595890212028, DIRECT, f08c47fec0942fa0"
        return HttpResponse(line)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)