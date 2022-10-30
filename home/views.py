from multiprocessing import context
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import LocationChoiceField, NewUserForm , CuisineChoiceField
from .models import  Restaurant,Review
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # data = Restaurant.objects.all()
    # context = {''}
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("error 404: credentials not found")
            return redirect('login_page')
    return render(request, 'log1.html')  # made chnages here for login temp


def logoutpage(request):
    logout(request)
    return redirect('home')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def restdata_show(request):
    data = Restaurant.objects.all()
    # print(data[1])
    context = {"restd": data}
    return render(request, 'restdata.html', context)

@login_required(login_url="login_page")
def search(request):

    cuisine_list = CuisineChoiceField()
    area_list = LocationChoiceField()
    if request.GET.get('cuisines') and request.GET.get('area'):
        selected_cuisine = request.GET.get('cuisines')
        selected_area = request.GET.get('area')
        query_results = Restaurant.objects.filter(cuisines = selected_cuisine,
                                                  area = selected_area)
    else:
        query_results = Restaurant.objects.all()
    context = {
        'query_results': query_results,
        'cuisine_list': cuisine_list,
        'area_list' : area_list,
    }
    return render(request,'menu.html', context)


@login_required(login_url="login_page")
def detail(request,pk):
    fetchData = Restaurant.objects.get(id=pk)   
    all_reviews = Review.objects.all()
    # print(review)
    
    name = get_object_or_404(Restaurant, id=pk)
    
    if request.method == "POST":
        stars = request.POST.get('stars',3)
        content = request.POST.get('content', '')
        review = Review.objects.create( user=request.user,name = name, content=content,stars=stars)
        review.save()
    context = {"fetchData":fetchData,"all_reviews":all_reviews}
                
        
    return render(request, 'rest_detail.html', context)


