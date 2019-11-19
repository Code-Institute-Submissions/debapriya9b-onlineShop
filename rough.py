def post_delete(request, pk):    
    """
    To delete a post
    """
    post = get_object_or_404(Post, pk=pk)
    author = post.objects.get(pk=pk)
    if request.user == author.user:
        post.delete()
        posts = Post.objects.filter(published_date__lte=timezone.now()
           ).order_by('-published_date')
        return render(request, "blogposts.html", {'posts': posts})
    else:
         messages.error(request, "User can only delete own post")