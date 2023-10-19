"""smallchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from debugapp.views import EventListenerClass, EventListenerPostback, NewTicketView, GetTeamDetails, WidgetView, MessagePort, SaveToDb, ReteriveMessage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event_listener/$', EventListenerClass.as_view(), name='index_response'),
    url(r'^get_team_details/$', GetTeamDetails.as_view(), name='get_team_details'),
    url(r'^new_ticket/$', NewTicketView.as_view(), name='new_ticket'),
    url(r'^chat_window/$', WidgetView.as_view(), name='widget_view'),
    url(r'^message_port/$', MessagePort.as_view(), name='message_port'),
    url(r'^configure/$', EventListenerPostback.as_view(), name='event_listener_postback'),
    url(r'^save_to_db/$', SaveToDb.as_view(), name='save_to_db'),
    url(r'^reterive_message/$', ReteriveMessage.as_view(), name='reterive_message'),
]
