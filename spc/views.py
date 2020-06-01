from django.http import HttpResponse
from django.shortcuts import render
import pickle

def index(request):
    return render(request, 'spc/index.html')



def mnnb(request):
    return render(request, 'mnnb/index.html')

def post_mnnb(request):
    model = pickle.load(open('spc/brains/mnnb_model.pkl', 'rb'))
    vector = pickle.load(open('spc/brains/transform.pkl', 'rb'))
    
    text = [request.POST['input']]
    vectorized_text = vector.transform(text)
    prediction = model.predict(vectorized_text)
    return render(request, 'mnnb/result.html', {'prediction':prediction[0], 'text':text[0]})
    

def lreg(request):
    return render(request, 'lreg/index.html')

def post_lreg(request):
    model = pickle.load(open('spc/brains/lreg_model.pkl', 'rb'))
    vector = pickle.load(open('spc/brains/transform.pkl', 'rb'))
    
    text = [request.POST['input']]
    vectorized_text = vector.transform(text)
    prediction = model.predict(vectorized_text)
    return render(request, 'lreg/result.html', {'prediction':prediction[0], 'text':text[0]})


def svm(request):
    return render(request, 'svm/index.html')

def post_svm(request):
    model = pickle.load(open('spc/brains/svm_model.pkl', 'rb'))
    vector = pickle.load(open('spc/brains/transform.pkl', 'rb'))
    
    text = [request.POST['input']]
    vectorized_text = vector.transform(text)
    prediction = model.predict(vectorized_text)
    return render(request, 'svm/result.html', {'prediction':prediction[0], 'text':text[0]})


def nltk(request):
    return render(request, 'nltk/index.html')

def bag_of_words(tweet):
    words_dictionary = dict([word, True] for word in tweet.split())    
    return words_dictionary

def post_nltk(request):
    model = pickle.load(open('spc/brains/nltk_model.pkl', 'rb'))
    
    text = request.POST['input']
    text_tokens = bag_of_words(text)
    prediction = model.classify(text_tokens)
    return render(request, 'nltk/result.html', {'prediction':prediction, 'text':text})










