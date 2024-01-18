# Virendra has created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index_two.html')

def about_us(request):
    return render(request, 'about.html')

def email(request):
    return render(request, 'email.html')

def facebook(request):
    return render(request, 'facebook.html')

# Better approach is to use multiple if statements
def analyse_text(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newline = request.GET.get('newlineremover', 'off')
    extraspace = request.GET.get('extraspaceremover', 'off')


    if (djtext == ''):
        analyzed = ""
        params = {'purpose': 'No text Found!', 'analyzed_text': analyzed}


    elif (extraspace == 'off' and newline == 'off' and uppercase == 'off' and removepunc == 'off'):
        analyzed = djtext
        params = {'purpose': 'No action Specified!', 'analyzed_text': analyzed}
           
    elif (extraspace == 'off' and newline == 'off' and uppercase == 'off' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    elif (extraspace == 'off' and newline == 'off' and uppercase == 'on' and removepunc == 'off'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Made Uppercase', 'analyzed_text': analyzed}

    elif (extraspace == 'off' and newline == 'off' and uppercase == 'on' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        removed_punc = ""
        for char in djtext:
            if char not in punctuations:
                removed_punc = removed_punc + char
        analyzed = ""
        for char in removed_punc:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations and Made Uppercase', 'analyzed_text': analyzed}

    elif (extraspace == 'off' and newline == 'on' and uppercase == 'off' and removepunc == 'off'):
        analyzed = djtext
        analyzed = analyzed.replace('%0D%0A',' ')
        params = {'purpose': 'Removed New Line(s)', 'analyzed_text': analyzed}
        
    elif (extraspace == 'off' and newline == 'on' and uppercase == 'off' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        analyzed = analyzed.replace('%0D%0A',' ')
        params = {'purpose': 'Removed Punctuations and New Line(s)', 'analyzed_text': analyzed}

    elif (extraspace == 'off' and newline == 'on' and uppercase == 'on' and removepunc == 'off'):
        analyzed = djtext
        new_text = analyzed.replace('%0D%0A',' ')
        analyzed = ''
        for char in new_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed New Line(s) and Made Uppercase', 'analyzed_text': analyzed}

    elif (extraspace == 'off' and newline == 'on' and uppercase == 'on' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        new_text = analyzed.replace('%0D%0A',' ')
        analyzed = ''
        for char in new_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations, New Line(s) and Made Uppercase', 'analyzed_text': analyzed}
        
    # Repeat all the conditions for Extraspace

    elif (extraspace == 'on' and newline == 'off' and uppercase == 'off' and removepunc == 'off'):
        analyzed = djtext
        analyzed = analyzed.replace('  ',' ') 
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
           
    elif (extraspace == 'on' and newline == 'off' and uppercase == 'off' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        analyzed = analyzed.replace('  ',' ') 
        params = {'purpose': 'Removed Punctuations and Extra Spaces', 'analyzed_text': analyzed}

    elif (extraspace == 'on' and newline == 'off' and uppercase == 'on' and removepunc == 'off'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        analyzed = analyzed.replace('  ',' ') 
        params = {'purpose': 'Made Uppercase and Removed Extra Spaces', 'analyzed_text': analyzed}

    elif (extraspace == 'on' and newline == 'off' and uppercase == 'on' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        removed_punc = ""
        for char in djtext:
            if char not in punctuations:
                removed_punc = removed_punc + char
        analyzed = ""
        for char in removed_punc:
            analyzed = analyzed + char.upper()
        analyzed = analyzed.replace('  ',' ') 
        params = {'purpose': 'Removed Punctuations, Extra Spaces and Made Uppercase', 'analyzed_text': analyzed}

    elif (extraspace == 'on' and newline == 'on' and uppercase == 'off' and removepunc == 'off'):
        analyzed = djtext
        analyzed = analyzed.replace('  ',' ')
        analyzed = analyzed.replace('%0D%0A',' ')
        params = {'purpose': 'Removed New Line(s) and Extra Spaces', 'analyzed_text': analyzed}
        
    elif (extraspace == 'on' and newline == 'on' and uppercase == 'off' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        analyzed = analyzed.replace('%0D%0A',' ')
        analyzed = analyzed.replace('  ',' ')
        params = {'purpose': 'Removed Punctuations, Extra Spaces and New Line(s)', 'analyzed_text': analyzed}

    elif (extraspace == 'on' and newline == 'on' and uppercase == 'on' and removepunc == 'off'):
        analyzed = djtext
        new_text = analyzed.replace('%0D%0A',' ')
        analyzed = ''
        for char in new_text:
            analyzed = analyzed + char.upper()
        analyzed = analyzed.replace('  ',' ')
        params = {'purpose': 'Removed New Line(s), Extra Spaces and Made Uppercase', 'analyzed_text': analyzed}

    elif (extraspace == 'on' and newline == 'on' and uppercase == 'on' and removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        new_text = analyzed.replace('%0D%0A',' ')
        analyzed = ''
        for char in new_text:
            analyzed = analyzed + char.upper()
        analyzed = analyzed.replace('  ',' ')
        params = {'purpose': 'Removed Punctuations, New Line(S), Extra Spaces and Made Uppercase', 'analyzed_text': analyzed}
        
    else:
        analyzed = ""
        params = {'purpose': 'Error!', 'analyzed_text': analyzed}
    
    return render(request, 'analyze_two.html', params)

