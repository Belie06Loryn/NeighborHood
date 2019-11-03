from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BusinessForm
from .models import Hood,Calls,Business


def page(request):
    hoods = Hood.objects.all()
    return render(request,'all-files/index.html',{"hoods":hoods})

@login_required(login_url='/accounts/login/')
def Hoo(request,pk):
    hoo = Hood.objects.get(id=pk)
    current_user = request.user
    busi=Business.objects.filter(id=hoods)
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user= current_user
            business.save()
        return redirect('hood')
    else:
        form =BusinessForm()
    return render(request, 'all-files/hood.html',{"hoo":hoo,"form": form,"busi":busi})  

# @login_required(login_url='/accounts/login/')
# def profile_display(request):
#    current_user = request.user
#    profile=Profile.objects.filter(username_id=current_user).first()
#    print(profile)
#    images=Foto.objects.filter(profile_id=current_user)
#    return render(request, 'all-files/post.html', {"images":images,"profile":profile})     

# def search_results(request):
#     if 'searchs' in request.GET and request.GET['searchs']:
#         search = request.GET.get("searchs")
#         searched = Foto.searchs(search)
        
#         backend = f"{search}"
        
#         return render(request, 'all-files/search.html',{"backend":backend,"searchs":searched})
    
#     else:
#         backend = "You haven't searched for any term"
#         return render(request, 'all-files/search.html',{"backend":backend})   