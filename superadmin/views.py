from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.models import Course, CourseOffer, CourseHistory
import datetime


def loginform(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		if username != "superadmin":
			login(request, superadmin)
			return redirect('superadmin_index')

		superadmin = authenticate(username=username, password=password)
		print(superadmin)
		if superadmin is not None:
			login(request, superadmin)
			return redirect('superadmin_index')
		else:
			messages.error(request,"Invalid Username and Password..")
			return redirect('superadmin_loginform')
	return render(request,"superadmin/login.html")



@login_required(login_url='superadmin_loginform')
def index(request):
	total_approved_courses = Course.objects.filter(approve=True).count()
	total_not_approved_courses = Course.objects.filter(approve=False).count()
	total_offers = CourseOffer.objects.all().count()
	total_sales = CourseHistory.objects.all().count()
	context={
		'home':True,
		'total_not_approved_courses':total_not_approved_courses,
		'total_approved_courses':total_approved_courses,
		'total_offers':total_offers,
		'total_sales':total_sales,
	}
	return render(request,"superadmin/index.html", context)


@login_required(login_url='superadmin_loginform')
def approved_course_list(request):
	courselist = Course.objects.filter(approve=True).order_by('-approval_datetime')
	total_course=courselist.count()
	context={
		"approvedcourse":True,
	'courselist':courselist,
	'total_course':total_course
	}
	return render(request,"superadmin/approved_course_list.html", context)

@login_required(login_url='superadmin_loginform')
def not_approved_course_list(request):
	courselist = Course.objects.filter(approve=False).order_by("-published_datetime")
	total_course=courselist.count()
	context={
		"not_approvedcourse":True,
	'courselist':courselist,
	'total_course':total_course
	}
	return render(request,"superadmin/not_approved_course_list.html", context)

@login_required(login_url='superadmin_loginform')
def approved(request, id):
	course = Course.objects.get(id=id)
	course.approve=True
	course.approval_datetime = datetime.datetime.now()
	course.save()
	return redirect("superadmin_not_approved_course_list")


@login_required(login_url='superadmin_loginform')
def course_offers(request):
	courselist = CourseOffer.objects.all()
	total_course=courselist.count()
	context={
		"course_offres":True,
	'courselist':courselist,
	'total_course':total_course
	}
	return render(request,"superadmin/course_offers.html", context)

@login_required(login_url='superadmin_loginform')
def course_selling_history(request):
	history_list = CourseHistory.objects.all()
	total_history=history_list.count()
	context={
	"course_offres":True,
	'history_list':history_list,
	'total_history':total_history
	}
	return render(request,"superadmin/course_selling_history.html", context)

