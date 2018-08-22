
from django.conf.urls import url
from django.contrib import admin
from decider.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^decider$', view=DeciderView.as_view(), name='decider'),
    url(r'^$', view=TemplateView.as_view(), name='tview'),
]
