from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LMS_for_MBMC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student_mgmt_app/', include('LMS_for_MBMC.student_mgmt_app.urls'))
)

if not settings.DEBUG:
    urlpattern += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
