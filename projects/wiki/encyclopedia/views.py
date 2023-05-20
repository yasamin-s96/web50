from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.files.storage import default_storage
from . import util
from markdown2 import Markdown


markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    title = title.lower()
    if not default_storage.exists(f"encyclopedia/templates/encyclopedia/{title}.html"):
        if title in util.list_entries():
            requested_entry = util.get_entry(title)
            html = markdowner.convert(requested_entry)
            util.write_html(title, html)        
        else:
            return HttpResponseNotFound()
    
    return render(request, f"encyclopedia/{title}.html")
        
        
    

