from django.shortcuts import render
from . import logic
import pyqrcode
from zxcvbn import zxcvbn
from django.shortcuts import HttpResponse
from PIL import Image 
# Create your views here.

def button(request):
        # form = PasswordForm()
        return render(request,'home.html')

def index(request):
        global data,length
        if request.method == "POST":
                length = request.POST["range"]
        data = logic.generate(int(length))
        data = str(data)        
        return render(request,'home.html',{'data':data})


def qrcode(request):        
        code = pyqrcode.create(data)
        code.show()
        return render(request,'home.html',{'data':data,'code':code})

def strength(request):
        pass_strength_info = zxcvbn(data)
        pass_strength_fast = pass_strength_info['crack_times_display']['offline_fast_hashing_1e10_per_second']
        pass_strength_slow = pass_strength_info['crack_times_display']['offline_slow_hashing_1e4_per_second']
        context = {
                'data':data,
                'pass_strength_fast':pass_strength_fast,
                'pass_strength_slow':pass_strength_slow,
        }
        return render(request,'home.html',context)

def secureImage(request):
        code = pyqrcode.create(data)
        code.png('code.png',scale=7)
        response = HttpResponse(content_type="image/png")
        img = Image.open('code.png')
        img.save(response,'png')
        return response