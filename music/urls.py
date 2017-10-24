from django.conf.urls import url
from music import views

app_name = 'music'

urlpatterns = [
    # /music/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='detail'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    # url(r'^(?P<pk>[0-9]+)/delete_song/$', views.DeleteSong, name='delete_song'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
]