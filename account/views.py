from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		user_name = request.POST['User Name']
		password1 = request.POST['Password']
		password2 = request.POST['Retype Password']
		try:
			User.objects.get(username=user_name)
			return render(request, 'signup.html', {'Wrong_username': 'This User Name has Exist'})
		except User.DoesNotExist:
			if password1 == password2:
				User.objects.create_user(username=user_name, password=password1)
				return redirect('mainpage')
			else:
				return render(request, 'signup.html', {'Wrong_password': 'Two passwords should be same'})