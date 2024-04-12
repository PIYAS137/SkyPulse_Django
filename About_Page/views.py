from django.shortcuts import render

# Create your views here.
def Render_AboutPage(req):

    return render(req,'About_Page/About_Page.html')