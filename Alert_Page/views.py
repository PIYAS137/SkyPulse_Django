from django.shortcuts import render

# Create your views here.
def Render_AlertPage(req):

    return render(req,'Alert_Page/Alert_Page.html')