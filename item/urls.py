# url() 関数のインポート
from django.conf.urls import url


from . import views


# ルーティングの設定 : hello/ というURLにアクセスがあった場合に hello() を呼び出す
urlpatterns = [
    # /post/ 以下に数字が渡された場合にマッチ
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    # /news/ 以下に文字列が渡された場合にマッチ
    url(r'^news/(?P<slug>[-\w]+)/$', views.news, name='news'),
]
