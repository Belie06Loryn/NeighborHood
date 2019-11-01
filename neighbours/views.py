from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import ProfileForm,FotoForm,VotingForm
# from .models import Profile,Foto,Voting


def page(request):
    # images=Foto.objects.all()
    # profile=Profile.objects.all()'images':images,'profile':profile
    return render(request,'all-files/index.html',{})

# def submit(request):
#     return render(request,'all-files/submit.html',{})       

# @login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user= current_user
#             profile.save()
#         return redirect('profile_display')
#     else:
#         form =ProfileForm()
#     return render(request, 'all-files/profile.html', {"form": form}) 

# @login_required(login_url='/accounts/login/')
# def profile_display(request):
#    current_user = request.user
#    profile=Profile.objects.filter(username_id=current_user).first()
#    print(profile)
#    images=Foto.objects.filter(profile_id=current_user)
#    return render(request, 'all-files/post.html', {"images":images,"profile":profile})

# @login_required(login_url='/accounts/login/')
# def project(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = FotoForm(request.POST,request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user= current_user
#             project.save()
#         return redirect('profile_display')
#     else:
#         form =FotoForm()
#     return render(request, 'all-files/project.html', {"form": form})       

# def search_results(request):
#     if 'searchs' in request.GET and request.GET['searchs']:
#         search = request.GET.get("searchs")
#         searched = Foto.searchs(search)
        
#         backend = f"{search}"
        
#         return render(request, 'all-files/search.html',{"backend":backend,"searchs":searched})
    
#     else:
#         backend = "You haven't searched for any term"
#         return render(request, 'all-files/search.html',{"backend":backend})   