#coding:utf-8 
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext
from bookmarks.forms import *

def register_page(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        variables = RequestContext(request, 
                    {'form': form}
        )
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            
            return render_to_response('registration/register_success.html' \
                , variables)
        else:
        
            return render_to_response(
                'registration/register.html', variables 
        )
    else:
        form = RegistrationForm()
        variables = RequestContext(request, 
                        {'form': form}
        )
        
        return render_to_response(
            'registration/register.html',
             variables
        )
        

def main_page(request):

    return render_to_response(
        'main_page.html',
        RequestContext(request),
    )

def user_page(request, username):
    
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404(u'Usuário não encontrado')
    
    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')
    variables = RequestContext(request, {
        'username': username,
        'bookmarks': bookmarks,
    })
    
    return render_to_response('user_page.html', variables)
    
def logout_page(request):

    logout(request)
    
    return HttpResponseRedirect('/')

def fechar_conta(request, username):

    user = User.objects.get(username=username)
    user.delete()
    logout(request)
    
    return HttpResponseRedirect('/')
