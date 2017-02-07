from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

# imports CBV(Class Based View) ListView
# is pre-built CBV provided by Django that has all
# of the functionality to achieve the goals of this view
from django.views.generic import ListView
# This tool provideds view security
# Ensures that only users who are authenticated havea access to the account list page
from django.contrib.auth.decorators import login_required
# method_decorators are used in conjunction with login_decorator
from django.utils.decorators import method_decorator

from .models import Post
from .forms import PostForm

# Create your views here.

# Subclass of ListView
class PostList(ListView):
	model = Post
	paginate_by = 3
	template_name = 'posts/post_list.html'
	# Give queried data name for use in template
	context_object_name = 'posts'

	# records for the current user only
	def get_queryset(self):
		post_list = Post.objects.filter(owner=self.request.user)
		return post_list

@login_required()
def post_create(request):
	if request.POST:
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.owner = request.user
			post.save()
			#redirect_url = post.get_absolute_url()
			redirect_url = reverse(
					'post_detail',
					args=(post.uuid,)
			)
			return HttpResponseRedirect(redirect_url)
	else:
		form = PostForm()

	variables = {
			'form' : form,
	}

	template = 'posts/post_create.html'

	return render(request, template, variables)

@login_required()
def post_detail(request, uuid):
	post = Post.objects.get(uuid=uuid)
	if post.owner != request.user:
		return HttpResponseForbidden()

	variables = {
		'post' : post,
	}

	return render(request, 'posts/post_detail.html', variables)