from django.shortcuts import render
import json

from django.http import HttpResponse
from django.shortcuts import render
from login.models import Department


def admin(request):
    pass


def edit(request):
    uid = request.session.get("user")

    if uid is not None:

        if request.method == "GET":
            id = request.GET.get("id"),
            print(id[0])
            department = Department.objects.filter(id=id[0]).get()

            print(department.workid)

            return render(request, "department.html", {'d': department})
        if request.method == "POST":
            id = request.POST.get("id"),
            depname = request.POST.get("depname")
            workid = request.POST.get("workid")
            topid = request.POST.get("topid")

            c = Department.objects.filter(id=id[0]).update(depname=depname,workid=workid,topid=topid)


            if c != 0:
                return HttpResponse("增加成功！")
            else:
                return HttpResponse("增加失败")

    else:

        return render(request, "login.html")


def delete(request):
    uid = request.session.get("user")

    if uid is not None:

        did = int(request.GET.get("id")[0]),

        print(request.GET.get("id"))

        print(did)

        c = Department.objects.get(id=did[0]).delete()

        if c != 0:
            return HttpResponse("删除成功！！")
        else:
            return HttpResponse("删除失败！！")
    else:

        return render(request, "login.html")


def add(request):
    uid = request.session.get("user")

    if uid is not None:

        if request.method == "GET":
            return render(request, "add_department.html")

        if request.method == "POST":

            depname = request.POST.get("depname")
            workid = request.POST.get("workid")
            topid = request.POST.get("topid")

            print(depname)

            department = Department(depname=depname,workid=workid, topid=topid)

            c = department.save()

            if c != 0:
                return HttpResponse("增加成功！！")
            else:
                return HttpResponse("增加失败！！")


    else:
        return render(request, "login.html")

