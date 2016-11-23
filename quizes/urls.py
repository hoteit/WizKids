from quizes import views
from django.conf.urls import include, url

urlpatterns = [url(r'^index/$', views.requires_login(views.problemsCntReport), name='index'),
   url(r'^login/$', views.login_user, name='login'),
   url(r'^logout/$', views.logout_user, name='logout'),
   url(r'^logout/$', views.logout_user, name='logout'),
   url(r'^nodatafound/$', views.nodata, name='nodata'),
   url(r'^dataerror/$', views.dataerror, name='dataerror'),
   url(r'^categories_list$', views.requires_login(views.ProblemCategoriesList.as_view()), name='categories_list'),
   url(r'^category_new$', views.requires_login(views.ProblemCategoryNew.as_view()), name='category_new'),
   url(r'^(?P<pk>\d+)/category_view/$', views.requires_login(views.ProblemCategoryView.as_view()), name='category_view'),
   url(r'^(?P<pk>\d+)/category_edit/$', views.requires_login(views.ProblemCategoryEdit.as_view()), name='category_edit'),
   url(r'^(?P<pk>\d+)/category_confirm_delete/$', views.requires_login(views.ProblemCategoryDelete.as_view()),
       name='category_delete'),
   url(r'^agegroups_list$', views.requires_login(views.ProblemAgeGroupsList.as_view()), name='agegroups_list'),
   url(r'^agegroup_new$', views.requires_login(views.ProblemAgeGroupNew.as_view()), name='agegroup_new'),
   url(r'^(?P<pk>\d+)/agegroup_view/$', views.requires_login(views.ProblemAgeGroupView.as_view()), name='agegroup_view'),
   url(r'^(?P<pk>\d+)/agegroup_edit/$', views.requires_login(views.ProblemAgeGroupEdit.as_view()), name='agegroup_edit'),
   url(r'^(?P<pk>\d+)/agegroup_confirm_delete/$', views.requires_login(views.ProblemAgeGroupDelete.as_view()),
       name='agegroup_delete'),
   url(r'^questions_list$', views.requires_login(views.ProblemQuestionsList.as_view()), name='questions_list'),
   url(r'^question_new$', views.requires_login(views.ProblemQuestionNew.as_view()), name='question_new'),
   url(r'^(?P<pk>\d+)/question_view/$', views.requires_login(views.ProblemQuestionView.as_view()), name='question_view'),
   url(r'^(?P<pk>\d+)/question_edit/$', views.requires_login(views.ProblemQuestionEdit.as_view()), name='question_edit'),
   url(r'^(?P<pk>\d+)/question_confirm_delete/$', views.requires_login(views.ProblemQuestionDelete.as_view()),
       name='question_delete'),
]

