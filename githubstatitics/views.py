from django.shortcuts import render

from django.shortcuts import render, redirect

from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

from .models import RepoTable
from django.contrib import admin
import requests
from django.http import HttpResponse
import pygal









def homepage(request):
        
      
      
      context = {
          
           
        }
      return render(request,  'home.html',  context)

  

  
  
 ############################# 
  
  
def all_repos(request):
    response = requests.get("https://api.github.com/users/Lucky-Yandy/repos")
    repos = response.json()

    for repo in repos:
        repo_name = repo['name']
        repo_star = repo['stargazers_count']
        repo_size = repo['size']
        repo_language = repo['language']

    context = {
        'repos': repos,
    }
     
    return render(request, 'allrepos.html', context)
  
  
  
  
  

def repo_size(request):
    response = requests.get("https://api.github.com/users/Lucky-Yandy/repos")
    repos = response.json()  
     
    repo_names = []
    repo_sizes = []
    for repo in repos:
        repo_names.append(repo['name'])
        repo_sizes.append(repo['size'])
    
    bar_chart = pygal.Bar(margin=50)
    bar_chart.title = 'Repo Size'
   
    bar_chart.x_labels = repo_names
    bar_chart.add('Size (bytes)', repo_sizes)
     
    chart_svg_as_datauri = bar_chart.render_data_uri()
       
    context = {
        'chart_svg_as_datauri': chart_svg_as_datauri
    }
    return render(request, 'reposize.html', context)
 
  
  
def repo_language(request):     
    response = requests.get("https://api.github.com/users/Lucky-Yandy/repos")
    repos = response.json()  
    
    repo_languages = []
    
    for repo in repos:
        language = repo['language']
        if language is not None:
            repo_languages.append(language)
    
    
    
    language_counts = {}
    for language in repo_languages:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1
    
    pie_chart = pygal.Pie()
    pie_chart.title = 'Repo Language'
    pie_chart.config.margin = 50
 
    for language, count in language_counts.items():
        pie_chart.add(language, count)
    
    chart_svg_as_datauri = pie_chart.render_data_uri()
       
    context = {
        'chart_svg_as_datauri': chart_svg_as_datauri
    }
    return render(request, 'repolanguage.html', context)





