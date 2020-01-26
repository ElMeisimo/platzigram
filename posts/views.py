from django.shortcuts import render
from datetime import datetime
# Create your views here.

def posts(request):
    postsList = [
        {
            "user": "Naruto",
            "name": "Naruto Uzumaki",
            "timestamp": datetime.now().strftime("%H:%m"),
            "photo": "https://picsum.photos/50/50/?image=1036",
            "picture": "https://picsum.photos/300/200/?image=1036",
        },
        {
            "user": "Sasuke",
            "name": "Sasuke Uchiha",
            "timestamp": datetime.now().strftime("%H:%m"),
            "photo": "https://picsum.photos/50/50/?image=903",
            "picture": "https://picsum.photos/300/200/?image=903",            
        },
        {
            "user": "Sakura",
            "name": "Sakura Haruno",
            "timestamp": datetime.now().strftime("%H:%m"),
            "photo": "https://picsum.photos/50/50/?image=1076",
            "picture": "https://picsum.photos/300/200/?image=1076",
        }
    ]

    
    return render(request, "feed.html", {"posts": postsList})