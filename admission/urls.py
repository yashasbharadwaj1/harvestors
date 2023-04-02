app_name = 'admission'
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('apply/', views.applyview,name='apply'),
    path('donate/', views.donate,name='donate'),
    path('thanks/',views.thanks),
    path('requestinfo/',views.requestinfo,name='info'),

    path('allalumni/',views.list_alumni,name='alumni'),
    path('allfaculties',views.list_faculties,name='faculty'),

    path('aboutus/',views.aboutus,name='about'),
    #C.th
    path('Certificate/',views.certificateinth,name='cth'),
    #D.th
    path('Diplomo/',views.diplomainth,name='dth'),
    #B.th
    path('Bachelor',views.bachelorinth,name='bth'),
    #M.div
    path('Divinity',views.mastersindivinity,name='mdiv'),

    #admission frequently asked questions
    path('admission',views.admissionfaq,name='faq')

]
