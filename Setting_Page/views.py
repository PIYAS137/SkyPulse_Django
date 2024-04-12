from django.shortcuts import render

# Create your views here.
def Render_SettingPage(req):

    return render(req,'Setting_Page/Setting_Page.html')