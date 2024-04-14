from django.shortcuts import render
from pydictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    antonyms = dictionary.antonym(search)
    synonyms = dictionary.synonym(search)

    context = {
        'meaning': meaning['Noun'][0],
        'antonyms': antonyms,
        'synonyms': synonyms,
    }
    return render(request, 'word.html', context)
