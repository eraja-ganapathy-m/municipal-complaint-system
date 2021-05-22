


from django.shortcuts import redirect, render
import datetime as dt
from myfirstapp.models import complaint, complaint_register, super_user_details


def concate(request):
    first_name=input()
    last_name=input()
    name=first_name.upper()+last_name.upper()
    print(name)
    
    person= {'fname':name}
    context= { 'person': person }
   
    return render(request,"upper.html",context)


#pub_from = request.GET.get('pub_date_from')


def com(request):
	if request.method=="GET":
		name=request.GET.get('name','')
		phone=request.GET.get('phone','')	
		types=request.GET.get('types','')
		desc=request.GET.get('desc','')
		area=request.GET.get('area','')
		ins=complaint_register(name=name,phone_no=phone,complaint_category=types,complaint_description=desc,area_of_complaint=area)
		ins.save()
	print("Data saved sucessfully")
	#return HttpResponse(" data inserted successfully")	
	return render(request, 'comp_form.html')



def userviewcomplaint(request):
	if request.method=="GET":
		name=request.GET.get('name')
		phone=request.GET.get('phone')
		com=complaint_register.objects.all().filter(phone_no=phone,name=name)
		data1=list()
		for i in com:
			if i.name != '':
				data1.append(i)
		stu = {
			"com_no": data1
        	}
		print(data1,"data view check")
		return render(request,"table.html",stu)
	return render(request,"user_view_detail.html")
	
	



def superuserlogin(request):
	error =[]
	
	if request.method=="POST":
			empid=request.POST['empid']
			passcode=request.POST['passcode']
			data = super_user_details.objects.all().filter(emp_id=empid,passcode=passcode)
			data1 = complaint_register.objects.all()
			list1=list()
			for i in data1:
				for j in data:	
					if i.complaint_category == j.department:
						list1.append(i)
			vu = {
				"view": data,
				"com_no":list1
        	}
			if data:
				return render(request, 'edit_table.html',vu)
			else:
				error.append(" Enter valid ID and Passcode ")
				return render(request,'super_user_login.html',{'error':error})

	return render(request,"super_user_login.html")






	


def update(request,Id):
	com=complaint_register.objects.get(id=Id)
	stu={
		"comp":com
	}
	print("outside post:",Id)
	if request.method=="POST":
		ack=request.POST['ack']
		status=request.POST['status']
		steps=request.POST['steps']
		print(Id,"id0001")
		update=dt.datetime.today()
		mon=update.strftime("%B")
		date=update.strftime("%d")
		year=update.strftime("%Y")
		dou=mon+" "+date+", "+year
		complaint_register.objects.filter(id=Id).update(acknowledgement_of_complaint=ack,complaint_status=status,steps_taken=steps,date_of_update=dou)
		com1=complaint_register.objects.all()
		com2=complaint_register.objects.filter(id=Id)
		list2=list()
		for i in com1:
			for j in com2:
				if i.complaint_category==j.complaint_category:
					list2.append(i)
		tb={
			"com_no":list2
		}
		return render(request,"edit_table.html",tb)
	
	return render(request,'update_save.html',stu)
