from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    url(r'^Call/$',views.Call,name = 'Call'),
    url(r'^Hoo/(?P<pk>\d+)$',views.Hoo,name="Hoo"),
    # url(r'^Vote/$',views.Vote,name="Vote"),
    # url(r'^search/$',views.search_results,name="search_results"), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)