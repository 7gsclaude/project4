# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post, Comment
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm



# # Define the home view
# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')


def home(request):
    return render(request, "home.html")

  
def about(request):
    return render(request, 'about.html')


# Add new view
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_index.html', {'posts': posts})

##helps handle the posts 



# # this detail function got updated at the very end in order to show the relationships between the medication

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  # create an instance of our feeding form
  return render(request, 'posts/post_detail.html', {
      'post': post
      ##comments 
  })
   
   
   
   
def signup(request):
 
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
      return redirect('index')
    # if the user inputs are invalid
    else:
      # generate error message to present to the screen
       error_message = 'somethings Invalid***'
  # send a new form to the template
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
      'form': form,
      'error': error_message
  })


def assoc_comment(request, post_id, comment_id):
  Post.objects.get(id=post_id).comment.add(comment_id)
  return redirect('detail', post_id=comment_id)


# def add_feeding(request, coral_id):
#     form = FeedingForm(request.POST)
#     if form.is_valid():
#         new_feeding = form.save(commit=False)
#         new_feeding.coral_id = coral_id
#         new_feeding.save()
#     return redirect('detail', coral_id=coral_id)

#     # for there to be a relationship between certain things,this must be established




class PostCreate(CreateView):
    model = Post
    fields = ('post_field',)
    success_url = '/posts/'
    
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ('post_field',)


class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/posts/'

# # todoo createing a coral landing sppot adn and trying to fix this error markdown is placed where it needs to be. should be bplaced

class CommentCreate (LoginRequiredMixin, CreateView):
    model = Comment
    fields = ("comment_field",)

class CommentDelete (LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/'


class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ('comment_field',)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  ##### TTO DOOOOO####
  
# FIGURE OUT THIS ERROR accounts/signup
