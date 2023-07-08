from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_view, name='main_view'),
    path('search/page/', views.search_page, name='search_page'),
    path('search/<category>/<board_type>/<post_type>/<search_type>/', views.search_posts, name='search_posts')
    # category: 구인/구직, board_type: Free/(구인/구직), post_type: 구인 -> 관심 분야/신입/경력, search_type: 검색 조건
]