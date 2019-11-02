from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import ProfileForm,FotoForm,VotingForm
from .models import Hood


def page(request):
    hoods = Hood.objects.all()
    return render(request,'all-files/index.html',{"hoods":hoods})

@login_required(login_url='/accounts/login/')
def Hoo(request,id):
    hoo = Hood.objects.filter(id=id)
    return render(request, 'all-files/hood.html',{"hoo":hoo})  

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
# def hoo(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = FotoForm(request.POST,request.FILES)
#         if form.is_valid():
#             hoo = form.save(commit=False)
#             hoo.user= current_user
#             hoo.save()
#         return redirect('profile_display')
#     else:
#         form =FotoForm()
#     return render(request, 'all-files/hoo.html', {"form": form})       

# def search_results(request):
#     if 'searchs' in request.GET and request.GET['searchs']:
#         search = request.GET.get("searchs")
#         searched = Foto.searchs(search)
        
#         backend = f"{search}"
        
#         return render(request, 'all-files/search.html',{"backend":backend,"searchs":searched})
    
#     else:
#         backend = "You haven't searched for any term"
#         return render(request, 'all-files/search.html',{"backend":backend})   