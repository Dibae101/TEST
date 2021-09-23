from django.shortcuts import render,redirect





# Create your views here.


from django import forms


# Create your views here.
from .models import Dept_list





def index(request):
	if request.user.is_authenticated:
		return redirect('/account/profile')
	data=Dept_list.objects.all();
	mydata={
	'data':data
	}
	return render(request,'index.html',context=mydata)



