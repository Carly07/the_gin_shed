from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from .forms import BlogPostForm, AddComment


def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
            ).order_by('-published_date')
    return render(request, "blog/blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the postdetail.html template.
    Or return a 404 error if the post is
    not found.
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    post_comments = PostComment.objects.filter(pk=pk).order_by(
        '-date_commented')

    if request.method == 'POST':
        create_comment_form = PostComment(
            comment_detail=request.POST.get('comment_detail'),
            user=request.user,
            post=post
        )
        create_comment_form.save()
        messages.success(request, 'Comment added to Post')
        return redirect('post_detail', pk)

    context = {
        'post': post,
        'form': AddComment,
        'comments': post_comments
    }
    return render(request, "blog/postdetail.html", context)


@login_required
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the post ID
    is null or not
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you do are not authorised to perform this action')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Success! Your Blog has been posted!')
            return redirect(post_detail, post.pk)
        else:
            messages.error(request, 'Oops! Failed to post blog. Please ensure the form is valid.')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blogpostform.html', {'form': form})


@login_required
def delete_post(request, pk):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you do are not authorised to perform this action')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('get_posts'))
