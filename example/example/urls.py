from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from ajax_select import urls as ajax_select_urls
from example import views

admin.autodiscover()

urlpatterns = [
                  url(r'^search_form',
                      view=views.search_form,
                      name='search_form'),
                  url(r'^admin/lookups/', include(ajax_select_urls)),
                  url(r'^admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
