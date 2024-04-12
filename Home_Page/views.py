from django.shortcuts import render

# Create your views here.
def Render_HomePage(req):

    return render(req,'Home_Page/Home_Page.html')