# created by samarth
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    #get the text
    djtext = (request.POST.get('text', 'errorrrr'))
    removepunc = (request.POST.get('removePunc', 'off'))
    fullcapitalize = (request.POST.get('fullcapitalize','off'))
    newline = (request.POST.get('newlinermv','off'))
    extraspaceremove = (request.POST.get('extraspacermv','off'))
    charstatus = (request.POST.get('charcount','off'))
    
    #analyze the text
    analyzed = ''
    if removepunc == 'on':
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext :
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext =analyzed

    if fullcapitalize == 'on':
        analyzed = djtext.upper()
        params = {'purpose':'Capitilized','analyzed_text':analyzed}
        djtext =analyzed
        
    if newline == 'on':
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char 
        params = {'purpose':'newline removed','analyzed_text':analyzed}
        djtext =analyzed
        
    if extraspaceremove == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed =analyzed +char
        params = {'purpose':'Extra Space Removed','analyzed_text':analyzed}
        djtext =analyzed
    
    # return if no option are selected
    if (removepunc != 'on' and fullcapitalize != 'on' and newline != 'on' and extraspaceremove != 'on') :
        return HttpResponse("Invalid option")
        
    return render(request,'analyze.html',params)