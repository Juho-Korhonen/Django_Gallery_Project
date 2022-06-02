from django.shortcuts import render
from .models import User,Picture


# Create your views here.
def display_gallerypage(request,user_name):

    poster = User.objects.get(username=user_name)
    pictures = Picture.objects.filter(poster=poster)
    return render(request, "gallerypage/gallerypage.html", {'poster': poster, 'pictures': pictures})


def display_specific_pic(request,user_name,specific_pic):
    poster = User.objects.get(username=user_name)
    specific_image = Picture.objects.get(poster=poster,text=specific_pic)

    return render(request, "gallerypage/inner_gallerypage.html", {'poster': poster, 'specific_image': specific_image})






