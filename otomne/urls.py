from django.urls import path

## added
from django.contrib.auth.views import login
#With django 1.10 I need to pass the callable instead of
#url(r'^login/$', 'django.contrib.auth.views.login', name='login')

from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
###


from . import views

app_name = 'otomne'

urlpatterns = [
    path('', views.index, name='index'),
    #path('fiche/', views.add_fiche, name='add_fiche'),
    #path('fiche/genpdf/<int:pk>/', views.genpdf, name='genpdf'),
    #path('page_prod/', views.page_prod, name='page_prod'),
    #path('add_child/', views.add_child, name='add_child'),
    #path('list/<int:n>', views.list_view, name='list'),
    # path('compilateurpdf/', views.compilateurpdf, name='compilateurpdf'),
    # path('generate/<file>', views.gen_pdf_old, name='generate'),
    # #path('main/<pk:int>/edit/', views.edit_emavitae, name='edit_emavitae'),
    # path('main/<int:pk>/', views.out_emavitae, name='out_emavitae'),
    # path('tutos/', views.Tutos_view, name='tutos_view'),
    # path('slides/<slug>/', views.slides_detail_slug, name='slides_detail_slug'),
    # path('slides/<slug>/<int:page>/', views.slides_detail_slug_page, name='slides_detail_slug_page'),
    # path('tutos/<int:pk>/', views.tutos_detail, name='tutos_detail'),
    # path('tutos/<slug>/', views.tutos_detail_slug, name='tutos_detail_slug'),
    # path('slides/<int:pk>/', views.slides_detail, name='slides_detail'),
    # path('slides/<int:pk>/edit/', views.edit_slides, name='edit_slides'),
    # path('main/edit/<int:pk>/', views.edit_emavitae, name='edit_emavitae'),
     #path('fiche/edit/<int:pk>/', views.edit_fiche, name='edit_fiche'),
    # path('fiche/edit_bis/<int:pk>/<int:n>/<int:vertex>/', views.edit_fiche_bis, name='edit_fiche_bis'),
     #path('fiche/fiche_detail_bis/<int:pk>/<int:n>/<int:vertex>/', views.fiche_detail_bis, name='fiche_detail_bis'),
    # path('main/pdf/<int:pk>/', views.gen_pdf, name='gen_pdf'),
    # path('taut/', views.taut, name='taut'),
    # path('example/', views.example, name='example'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('user_login/', views.user_login, name='user_login'),
    #path('login/', login, name='login'),
    #path('logout/', logout,name='logout'),
    #path('logout-then-login/', logout_then_login,name='logout-then-login'),
]
