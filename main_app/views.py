# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
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

# def post_detail(request, post_id, comment_id):
#   post = Post.objects.get(id=post_id)
#   comments = Comment.objects.get(id=comment_id)
 
#   # if im going to use the above i need to  uncomment adn apply commentid to the () 
#   # create an instance of our feeding form
#   return render(request, 'posts/post_detail.html', {
#       'post': post,
#       'comments': comments
      
#   })   
  
  
#   ###below is the post detail pulled from a django comment and posting example 
def post_detail(request, slug):
  template_name = 'post_detail.html'
  post = get_object_or_404(Post, slug=slug)
  comments = post.comments.filter(active=True)
  new_comment = None
    # Comment posted
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():

            # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
      new_comment.post = post
            # Save the comment to the database
      new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "posts/detail.html", {'post': post,
                                                 'comments': comments,
                                                 'comment_form': comment_form})
  
  
  
    
  

def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'main_app/comment_detail.html', {'comment': comment})
   
   
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  ##### TTO DOOOOO####
  
# FIGURE OUT THIS ERROR accounts/signup
