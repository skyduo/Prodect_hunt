from django.shortcuts import render

# Create your views here.


def product_list(request):
	return render(request, 'product_list.html')


def publish(request):
	if request.method == 'GET':
		return render(request, 'Publish.html')
	elif request.method == 'POST':
		product_name = request.POST['Product Name']
		introduction = request.POST['Introduction']
		product_link = request.POST['Product Link']
		product_icon = request.FILES['Product icon']
		Image = request.FILES['Image']
		return render(request, 'publish.html')