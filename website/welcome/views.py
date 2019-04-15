from django.shortcuts import render

# Create your views here.
def display(req,username):
	print(username)
	return render(req,"home.html",{"username":username})