from django.urls import path
from .views import new_list, new_detail, HomePageView,  contactPageView, errot404page, about_view, LocalNewsView, ForeignNewsView, TechnologyNewsView, SportNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', new_list, name="all_news_list"),
    path('news/<slug:news>/', new_detail, name="news_detail_page"),
    path('contact-us/', contactPageView.as_view(), name="contact_page"),
    path('error/', errot404page, name='error_page'),
    path('about/', about_view, name='about_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreignnews/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),

]