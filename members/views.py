from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from members.models import Member

def index(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request,"index.html",context)

def create(request):
    if request.method == 'POST':
        phone= request.POST.get("phone")
        if Member.objects.filter(phone=phone).exists():
            messages.error(request, "Phone already registered!")
            return render(request, 'create_member.html')
        else:
            member = Member()
            member.firstname = request.POST.get('firstname')
            member.lastname = request.POST.get('lastname')
            member.phone = request.POST.get('phone')
            member.save()
            messages.success(request, "Patient  added successfully!")
            return HttpResponseRedirect('index')
    
    return render(request, "create_member.html")

def detail(request,id):
    member = Member.objects.get(id=id)
    if member != None:
        return render(request, 'detail_customer.html', {"member": member})
    
def edit(request,id):
    member = Member.objects.get(id=id)
    if member != None:
        return render(request, 'edit_customer.html', {"member": member})

def update(request):
    if request.method == 'POST':
        member = Member.objects.get(id = request.POST.get('member_id'))
        if member != None:
            member.firstname = request.POST.get('firstname')
            member.lastname = request.POST.get('lastname')
            member.phone = request.POST.get('phone')
            member.save()

            messages.success(request, "Member  update successfully!")
            return HttpResponseRedirect('index')
        
def delete(request):
    if request.method == "POST":
        patient = Member.objects.get(id=request.POST.get("member_id"))
        patient.delete()
        messages.success(request, "Member removed successfully!")
        return HttpResponseRedirect('index')