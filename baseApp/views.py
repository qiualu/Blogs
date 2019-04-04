from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response


#404页面
# @csrf_exempt
# def page_not_found(request):
#     return render_to_response('baseApp/404.html')

# def index(request):
#     return HttpResponse(u"欢迎光临 自强学堂!")

def index(request):
    return render(request, 'baseApp/404.html')
    # return render(request, 'home.html')

# @csrf_exempt
# def page_error(request):
#     return render_to_response('500.html')




