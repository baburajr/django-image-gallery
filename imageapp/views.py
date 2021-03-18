from django.shortcuts import render
from .forms import ImageForm
from .models import Images
# Create your views here.

def home(request):
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    form = ImageForm()
    img = Images.objects.all().order_by('-id')
  else:
    form=ImageForm()
    img = Images.objects.all().order_by('-id')
  return render(request, 'index.html', {'img':img, 'form':form})