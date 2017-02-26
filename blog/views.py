from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
import requests
url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
query = '''SELECT DISTINCT ?countryLabel ?headOfStateLabel
{
  ?country wdt:P31 wd:Q6256;
           wdt:P35 ?headOfState .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru" }
}
ORDER BY ?countryLabel
LIMIT 100
'''
data = requests.get(url, params={'query': query, 'format': 'json'}).json()
presidents = []
for item in data['results']['bindings']:
    presidents.append({
        'country': item['countryLabel']['value'],
        'head of state': item['headOfStateLabel']['value']})

def post_list(request):
    me = User.objects.get(username='tanya95')
    Post.objects.create(author=me, title='Sample title2', text='Test2')
    Post.objects.create(author=me, title='Sample title3', text='Test3')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})