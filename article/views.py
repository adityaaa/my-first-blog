from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from article.models import Article
from article.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def home(request):
	return render(request, "home.html")



def hello_template_simple(request):
	name = "aditya"
	return render_to_response('hello.html',{"name":name})



def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']	
		
	return render_to_response('articles.html',
							 {'articles': Article.objects.all(),"article":Article.objects.get(id=11),
							 'language' : language,
							 'session_language' : session_language})

def article(request,article_id=1):
	return render_to_response('article.html',{"article": Article.objects.get(id=article_id) })

def language(request, language = 'en-gb'):
	response = HttpResponse("setting language to %s" % language)

	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response

def create(request):
	if request.POST:
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/articles/all')
		else:
			form = ArticleForm()

		args = {}
		args.update(csrf(request))

		args['form'] = form

		return render_to_response('create_article.html', args)	

def like_article(request,article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count =a.likes
		count +=1
		a.likes = count
		a.save()

	return HttpResponseRedirect('/articles/get/%s' % article_id) 

def search_title(request):
	if request.method == 'GET':
		search_text = request.GET['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(title__contains=search_text)

	return render_to_response('search.html',{'articles':articles})	