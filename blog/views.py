from django.shortcuts import render, redirect
from blog.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, "post_list.html", {"posts":posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, "post_detail.html", {"post":post})
	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	print(post)
    
	if request.method == "POST":
		title=request.POST.get('title')
		text=request.POST.get('text')

		post.title=title
		post.text=text
		post.save()
		
		base_url = '/post/'     #post url
		query_string =  post.pk #post_id
		url = '{}{}'.format(base_url, query_string) #concat post url and post id 
		return redirect(url)
		
	return render(request, 'post_edit.html', {'post': post})
	
def post_new(request):
    if request.method == "POST":
        title=request.POST.get('title')
        text=request.POST.get('text')
        post = Post.objects.create(title=title,text=text)
        post.save()
        return redirect('/postlist/')
    
    return render(request, 'post_edit.html')