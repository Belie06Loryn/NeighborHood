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
    # busi=Business.objects.filter(),"busi":busi
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user= current_user
            business.save()
        return redirect('Hoo',pk)
    else:
        form =BusinessForm()
    return render(request, 'all-files/hood.html',{"hoo":hoo,"form": form})  
    

# def search_results(request):
#     if 'searchs' in request.GET and request.GET['searchs']:
#         search = request.GET.get("searchs")
#         searched = Foto.searchs(search)
        
#         backend = f"{search}"
        
#         return render(request, 'all-files/search.html',{"backend":backend,"searchs":searched})
    
#     else:
#         backend = "You haven't searched for any term"
#         return render(request, 'all-files/search.html',{"backend":backend})   