from django.http import JsonResponse

def home(request):
    return JsonResponse({'APIs':['fruit','region']})