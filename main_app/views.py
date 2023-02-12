# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm 



# # Define the home view
# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')


def home(request):
    return render(request, "home.html")

  
def about(request):
    return render(request, 'about.html')


# Add new view
@login_required
def post_index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'posts/post_index.html', {
      'posts': posts,
      'comments': comments
      })
     

##helps handle the posts 

def get_comments(self):
    return self.comment_set.all()



# # this detail function got updated at the very end in order to show the relationships between the medication

@login_required
def post_detail(request, post_id,):
  post = Post.objects.get(id=post_id)
  comments = reversed(Comment.objects.all())
  # if im going to use the above i need to  uncomment adn apply commentid to the () 
  # create an instance of our feeding form
  return render(request, 'posts/post_detail.html', {
      'post': post,
      # 'comments': comments
      'comments': comments
  })   
 

def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'main_app/comment_detail.html', {'comment': comment})
   
   
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # handle the creation of the new user
    # capture form inputs from the submission
    form = UserCreationForm(request.POST)
    # validate form inputs
    if form.is_valid():
      # save the new user
      user = form.save()
      # login the new user
      login(request, user)
      # redirect to the cats index
      return redirect('post_index')
    # if the user inputs are invalid
    else:
      # generate error message to present to the screen
      error_message = 'invalid credentials'
  # send a new form to the template
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
      'form': form,
      'error': error_message
  })

@login_required
def assoc_comment(request, post_id, comment_id):
  Post.objects.get(id=post_id).comment.add(comment_id)
  return redirect('detail', post_id=post_id)




class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('post_field',)
    success_url = '/posts/'
    
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ('post_field',)


class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/posts/'
  
# class CommentDetail (LoginRequiredMixin, DetailView):
#     model = Comment
#     fields = ("comment_field",)
    
class CommentCreate (LoginRequiredMixin, CreateView):
    model = Comment
    fields = ("comment_field",)

class CommentDelete (LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/'


class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ('comment_field',)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  ##### #########TTO DOOOOO####
  
# get heroku 
# working on css 

