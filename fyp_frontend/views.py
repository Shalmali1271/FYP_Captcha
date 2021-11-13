from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from .models import Captcha

def index(request) :
    arr = ['dog', 'cat', 'tree', 'road', 'bicycle', 'panda']
    ran_arr = random.choice(arr)
    s = True

    keywords = Captcha.objects.filter(key__icontains = ran_arr).order_by('?')[:3]
    ids = keywords.values_list('pk', flat=True)

    # Getting the random 6 images from rest of the images
    rest_img = random.choices([i for i in range(1,36) if i not in ids], k = 6)
    imgs = Captcha.objects.filter(pk__in = rest_img).order_by('?')

    final_imgs = keywords | imgs 
    
    temp = 0
    for i in final_imgs :
        if i.key == keywords.key :
            temp = temp + 1
        else : pass 

    # checking the output of the user.
    c = request.POST.get('randomly_arr')
    if request.POST.getlist('recommendations') == [c]*temp :
        return redirect(success)
    else : pass

    context = {
        'ran_arr': ran_arr,
        'final_imgs' : final_imgs,
    }
    return render(request, 'fyp_frontend/home.html', context)

def success(request) :
    return render(request, 'fyp_frontend/successful.html')
    
