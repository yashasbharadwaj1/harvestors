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
    path('admission',views.admissionfaq,name='faq'),

    path('coursesdata',views.course_details,name='course_details'),

    path('podcast',views.podcast,name="podcast"),
    path('photogallery',views.photogallery,name="gallery"),
    path('placementcell',views.placementcell,name="pc"),
    path('visit',views.visit,name="visit"),
    #api
    path('podcastdata',views.data_for_podcast,name='data_for_podcast'),
    path('gallerydata',views.data_for_photogallery,name='gallerydata'),
    path('t',views.t)

]
