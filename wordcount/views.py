import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'a': 'b'})


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordList = fulltext.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            # increase
            wordDictionary[word] += 1
        else:
            # add to dictionary
            wordDictionary[word] = 1
    sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'count' : len(wordList), 'wordDictionary' : sortedWords})


def about(request):
    return render(request, 'about.html')