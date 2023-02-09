# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post 
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
      return redirect('index')
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


# def add_feeding(request, coral_id):
#     form = FeedingForm(request.POST)
#     if form.is_valid():
#         new_feeding = form.save(commit=False)
#         new_feeding.coral_id = coral_id
#         new_feeding.save()
#     return redirect('detail', coral_id=coral_id)

#     # for there to be a relationship between certain things,this must be established


# def assoc_med(request, coral_id, med_id):
#   Coral.obejcts.get(id=coral_id).med.add(med_id)
#   return redirect('detail', cat_id=med_id)


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'

# class CoralCreate(CreateView):
#     model = Coral
#     fields = '__all__'
#     success_url = '/corals/'

   # this form takes the self anf form
#    renders a form with the users instance from the selfs user request

# this function is for the user auth i believe
#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        #to hand this back to wehere its pulled you involk super
#        return super().form_valid(form)


# class CoralUpdate(UpdateView):
#   model = Coral
#   # Let's disallow the renaming of a cat by excluding the name field!
#   fields = ['name', 'description', 'species', 'price']


# class CoralDelete(DeleteView):
#   model = Coral
#   success_url = '/corals/'


# # todoo createing a coral landing sppot adn and trying to fix this error markdown is placed where it needs to be. should be bplaced


# class MedsIndex(LoginRequiredMixin, ListView):
#   model = Meds


# class MedsCreate (LoginRequiredMixin, CreateView):
#   model = Meds
#   fields = '__all__'


# class MedsDetail(LoginRequiredMixin, DetailView):
#   model = Meds


# class MedsDelete(LoginRequiredMixin, DeleteView):
#   model = Meds
#   success_url = '/meds/'


# class MedsUpdate(LoginRequiredMixin, UpdateView):
#   model = Meds
#   fields = '__all__'