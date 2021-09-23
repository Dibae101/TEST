from django.shortcuts import render,redirect,get_object_or_404,redirect

from django.http import HttpResponse

# Create your views here.
from .forms import LoginForm,LoginForm1,Signup,Signup1,Signup2,Signup3
from django.contrib.auth import authenticate,login as auth_login,logout
from dept_list .models import Dept_list

from django import forms



def login_user(request,user_name):
	if request.user.is_authenticated:
		return redirect('/account/profile')
	if request.method=='POST':
		
		
		form = LoginForm(request.POST)
		form1 = LoginForm1(request.POST)
		if form.is_valid():
			if form1.is_valid():
				user=authenticate(username=form.cleaned_data['username'],password=form1.cleaned_data['password'])

				if user:
					print("is user")
					auth_login(request,user)
					return redirect('/account/profile')
				else:
					print("invalid user")
					return HttpResponse("invalid user refresh page to continue")
					return redirect('/account/login') 
					


			else:
				return HttpResponse("pw not valid refresh page to continue")
				print("pw not valid")
				return redirect('/account/login')
		else:
			return HttpResponse("username not valid refresh page to continue")
			print("username not valid")
			return redirect('/account/login')					
				# print(form.cleaned_data)
				# print(form1.cleaned_data)

	
	userobj=get_object_or_404(Dept_list,name=user_name)
		
		

	 	
	data=LoginForm()
	data2=LoginForm1()
	mydata={
	'form':data,
	'form1':data2,
	'userobj':userobj

	}
	return render(request,'account/login_tu.html',context=mydata)




def profile(request):
	if request.user.is_authenticated:
		return render(request,'account/profile.html')
	else:
		return redirect('/')	
			
	
 
	




def signup(request):
	data=Signup()
	data1=Signup1()
	data2=Signup2()
	data3=Signup3()
	form = Signup(request.POST)
	form1 = Signup1(request.POST)
	form2= Signup2(request.POST)
	form3 = Signup3(request.POST)
	if request.method=='POST':
		if form1.is_valid() and form.is_valid() and form2.is_valid() and form3.is_valid():
			print("valid")
			from django.contrib.auth.models import User
			if(User.objects.filter(username=form3.cleaned_data['username']).exists()):
				print("Exist")
			user = User(username = form1.cleaned_data['username'],
				first_name=form2.cleaned_data['firstname'],
				last_name=form3.cleaned_data['lastname'])
				
			user.save()
			user.set_password(form.cleaned_data['password'])
			user.save()

				

		
		else:
			print("invalid")	
	mydata={
	'form':data2,
	'form1':data3,
	'form2':data1,
	'form3':data,
	}
	return render(request,'account/signup_tu.html',context=mydata)


def log_out(request):
	logout(request)
	return redirect('/')	



