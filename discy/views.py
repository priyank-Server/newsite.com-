from django.shortcuts import render, redirect
from .models import *
from django.views import View, generic
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, Askquestion, Postanswer
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class IndexView(View):
    template_name = 'discy/index.html'

    def get(self, request, *args, **kwargs):
        answers = Answer.objects.all()
        queryset = Question.objects.all()
        recent_question = Question.objects.order_by('-pub_date')[:2]
        recent_answer = Answer.objects.order_by('-pub_date')[:1]

        return render(request, 'discy/index.html',
                      {'questions': queryset, 'recent_question': recent_question, "user": request.user,
                       'answers': answers,
                       "recent_answer": recent_answer})


def index1(request):
    return render(request, 'discy/index1.html')


class AskQuestionView(View):
    form_class = Askquestion
    template_name = 'discy/index1.html'
    success_url = reverse_lazy('discy:index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('discy:askquestion')
        return redirect('discy:index')


class AnswerView(View):
    form_class = Postanswer
    template_name = 'discy/index.html'
    success_url = reverse_lazy('discy:index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('discy:index')

        return redirect('discy:index')


class SignUpView(FormView):
    template_name = 'discy/index.html'
    form_class = UserForm
    success_url = reverse_lazy('discy:index')

    def form_valid(self, form):
        form.save()
        user = MyUser.objects.get(email=form.data.get('email'))
        user.is_active = True
        user.set_password(form.data.get('password'))
        user.save()
        return super(SignUpView, self).form_valid(form)


class LoginView(View):
    template_name = 'discy/index.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            print("user created")
            return redirect('discy:index')

        else:
            return redirect('discy:index')


class LogoutView(View):
    template_name = 'discy/index.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('discy:index')


class SearchView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET['query']
        recent_answer = Answer.objects.order_by('-pub_date')[:1]
        answers = Answer.objects.all()
        searched = Question.objects.filter(
            question_text__icontains=query
        )
        return render(request, 'discy/search.html', {'searched': searched, 'recent_answer': recent_answer,
                                                     'answers': answers})
