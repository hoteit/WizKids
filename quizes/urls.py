from quizes import views
from django.conf.urls import include, url

urlpatterns = [url(r'^index/$', views.requires_login(views.problemsCntReport), name='index'),
   url(r'^login/$', views.login_user, name='login'),
   url(r'^logout/$', views.logout_user, name='logout'),
   url(r'^logout/$', views.logout_user, name='logout'),
   url(r'^nodatafound/$', views.nodata, name='nodata'),
   url(r'^dataerror/$', views.dataerror, name='dataerror'),
   url(r'^problemCategories_list$', views.requires_login(views.ProblemCategoriesList.as_view()), name='problemCategories_list'),
   url(r'^problemCategory_new$', views.requires_login(views.ProblemCategoryNew.as_view()), name='problemCategory_new'),
   url(r'^(?P<pk>\d+)/problemCategory_view/$', views.requires_login(views.ProblemCategoryView.as_view()), name='problemCategory_view'),
   url(r'^(?P<pk>\d+)/problemCategory_edit/$', views.requires_login(views.ProblemCategoryEdit.as_view()), name='problemCategory_edit'),
   url(r'^(?P<pk>\d+)/problemCategory_confirm_delete/$', views.requires_login(views.ProblemCategoryDelete.as_view()),
       name='problemCategory_delete'),
   url(r'^problemAgeGroups_list$', views.requires_login(views.ProblemAgeGroupsList.as_view()), name='problemAgeGroups_list'),
   url(r'^problemAgeGroup_new$', views.requires_login(views.ProblemAgeGroupNew.as_view()), name='problemAgeGroup_new'),
   url(r'^(?P<pk>\d+)/problemAgeGroup_view/$', views.requires_login(views.ProblemAgeGroupView.as_view()), name='problemAgeGroup_view'),
   url(r'^(?P<pk>\d+)/problemAgeGroup_edit/$', views.requires_login(views.ProblemAgeGroupEdit.as_view()), name='problemAgeGroup_edit'),
   url(r'^(?P<pk>\d+)/problemAgeGroup_confirm_delete/$', views.requires_login(views.ProblemAgeGroupDelete.as_view()),
       name='problemAgeGroup_delete'),
   url(r'^problemQuestions_list$', views.requires_login(views.ProblemQuestionsList.as_view()), name='problemQuestions_list'),
   url(r'^problemQuestion_new$', views.requires_login(views.ProblemQuestionNew.as_view()), name='problemQuestion_new'),
   url(r'^(?P<pk>\d+)/problemQuestion_view/$', views.requires_login(views.ProblemQuestionView.as_view()), name='problemQuestion_view'),
   url(r'^(?P<pk>\d+)/problemQuestion_edit/$', views.requires_login(views.ProblemQuestionEdit.as_view()), name='problemQuestion_edit'),
   url(r'^(?P<pk>\d+)/problemQuestion_confirm_delete/$', views.requires_login(views.ProblemQuestionDelete.as_view()),
       name='problemQuestion_delete'),
]

