from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
def count(request):
    data = request.GET['fulltext']
    word_list = data.split()
    list_lenght = len(word_list)

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            #increase by 1
            word_dictionary[word] += 1
        else:
            #add ti dict
            word_dictionary[word] = 1

    sorted_list = sorted(word_dictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':data, 'list_length':list_lenght, 'word_dictionary':sorted_list})

def about(request):
    return render(request, 'about.html')