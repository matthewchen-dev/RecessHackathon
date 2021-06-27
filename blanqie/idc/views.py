from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Doc
from rake_nltk import Rake

# Create your views here.


def home(request):
    return render(request, 'idc/home.html')

def learn(request):
    return render(request, 'idc/learn.html')

def test(request):
    return render(request, 'idc/test.html')

class MainView(TemplateView):
    template_name = 'idc/test.html'

def file_upload_view(request):
    #print(request.FILES)

    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Doc.objects.create(name = 'notes', upload = my_file)
        return HttpResponse('upload')
    return JsonResponse({'post': 'false'})


all_entries = Doc.objects.last().upload
all_entries.open(mode = 'r+')

lines = all_entries.read()


r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
r = Rake(min_length=1, max_length=2)

print(r.extract_keywords_from_text(lines))
print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases_with_scores())



for word in r.get_ranked_phrases():
    
    if word in lines:
        lines = lines.replace(word, '_'*len(word))
        #all_entries.write(lines.replace(word, '_'*len(word)))

print(lines)
all_entries.seek(0)
all_entries.truncate(0)
all_entries.write(lines)
all_entries.close()

