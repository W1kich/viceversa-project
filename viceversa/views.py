from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def reverse(request):
	usertext = request.GET['usertext']
	reversrd_text = usertext[::-1]
	return render(request, 'reverse.html', {'usertext': usertext ,'reversetet': reversrd_text })