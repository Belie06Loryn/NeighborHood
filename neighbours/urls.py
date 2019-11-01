from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    # url(r'^profile/$',views.profile,name = 'profile'),
    # url(r'^profile_display/$', views.profile_display, name='profile_display'),
    # url(r'^project/$', views.project, name='project'),
    # url(r'^ProjectVote/(?P<pk>\d+)$',views.ProjectVote,name="ProjectVote"),
    # url(r'^Vote/$',views.Vote,name="Vote"),
    # url(r'^search/$',views.search_results,name="search_results"), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)