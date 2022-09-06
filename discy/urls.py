from django.urls import path
from discy import views
app_name = 'discy'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signout/', views.LogoutView.as_view(), name='signout'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('index1/', views.index1, name='index1'),
    path('askquestion/', views.AskQuestionView.as_view(), name='askquestion'),
    path('postanswer/', views.AnswerView.as_view(), name='postanswer'),
    path('search/', views.SearchView.as_view(), name='search'),

]

