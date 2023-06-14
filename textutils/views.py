#I have created this file - Surab
from django.http import HttpResponse
from django.shortcuts import render
#Code for personal navigator
#def index(request):
 #   return HttpResponse('''<h1>Surab<h1> 
   # <h2>Django course</h2>
  #  <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Code With Harry </a>
#<h2>Time-Pass</h2>
 #   <a href="https://www.instagram.com/">Instagram</a> 
  #  <h2>Web Dev course</h2>
   # <a href="https://cs50.harvard.edu/web/2020/weeks/3/"> CS50 Course</a>''')
                        
#def ron(request):
 #   return HttpResponse("Hello Ron ")


def index(request):
    #return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    #get the text and analyze the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    spaceremove = request.POST.get('spaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')
    charatercounter = request.POST.get('charatercounter','off')
    print(removepunc)
    print(fullcaps)
    print(spaceremove)
    print(newlineremove)
    print(charatercounter)
    print(djtext)
    
    punctuation = '''!()-[]{};:'"\,<>.?/@#$%^&*_~'''
    analyzed = djtext
   

    if (removepunc == "on"):
        for char in analyzed:
            if char in punctuation:
                analyzed = analyzed.replace(char, '')
        
    
    if (fullcaps == "on"):
        for char in analyzed:
            analyzed = analyzed.replace(char, char.upper())
            
        
    
    if (spaceremove == "on"):
        for char in analyzed:
            if char == " ":
                analyzed = analyzed.replace(char,'')
        
    
    if(newlineremove == "on"):
        for char in analyzed:
            if char == "\n" and char == "\r":
                analyzed = analyzed.replace(char, '')

    
    if(removepunc == "off" and newlineremove == "off" and spaceremove == "off" and fullcaps == "off"):
        return HttpResponse("<h2>Please choose a option...<h2>")
        
    
    
    if(charatercounter == "on"):
        count = 0
        for char in analyzed:
            count = count + 1
        params = {'purpose':'Analysis of the text', 'analyzed_text': analyzed,'Character_count':f'The no of charater in the analysed string is {count}'}
        return render(request, 'analyze.html',params)
    else:
        params = {'purpose':'Analysis of the text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
