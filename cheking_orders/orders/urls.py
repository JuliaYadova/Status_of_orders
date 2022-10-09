from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    # страница с тремя ссылками -
    # годы/загрузка/выгрузка (только авторизированным всё).
    path('', views.index, name='index'),
    # страница со списком годов и статусом года (done/ not done)
    path('years/', views.years_list, name='years_list'),
    # Отдельная страница с информацией о конкретном годе
    # и статусом месяца (done/ not done)
    path('years/<int:year>/', views.months_list, name='months_list'),
    # страница со списком заказов за месяц и статусом заказов (done/ not done)
    path('years/<int:year>/<int:month>/',
         views.month_list_orders,
         name='month_list_orders'),
    # страница с тремя полями для загрузки данных
    # СКД/Али/Претензия
    path('upload/', views.upload, name='upload'),
    # страница с фильтром данных и выгрузкой данных по филтру
    # поля фильтра год/все месяцы или конкретный/статус заказов все или нет
    path('download/', views.download, name='download'),
    path('upload/upload_vendor/', views.upload_vendor, name='upload_vendor'),
    path('upload/upload_market/', views.upload_market, name='upload_market'),
    path('upload/upload_return/', views.upload_return, name='upload_return'),
    path('upload/upload_claim/', views.upload_claim, name='upload_claim'),
]
