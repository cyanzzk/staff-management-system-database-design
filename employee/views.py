import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from employee import models
from eploman import settings
from eploman.settings import BASE_DIR


def edit(request):
    uid = request.session.get("user")

    if uid is not None:

        if request.method == 'GET':  # 获取本人信息页面，GET

            # 同时返回个人信息数据给前端

            print(uid)

            employee = models.Employee.objects.get(uid=uid)

            return render(request, "employee.html", {'e': employee})
        if request.method == 'POST':  # 修改本人信息
            id = int(request.POST.get("id")[0])
            password = request.POST.get("password")
            empname = request.POST.get("empname")
            sex = request.POST.get("sex")
            birth = request.POST.get("birth")
            img = request.POST.get("img")
            nation = request.POST.get("nation")
            empstatus = request.POST.get("empstatus")
            edu = request.POST.get("edu")
            address = request.POST.get("address")
            merr = request.POST.get("merr")
            idcard = request.POST.get("idcard")
            phone = request.POST.get("phone")
            idAddress = request.POST.get("idAddress")
            idwork = request.POST.get("idwork")
            datework = request.POST.get("datework")
            postwork = request.POST.get("postwork")
            levelwork = request.POST.get("levelwork")

            print(request.POST.get("topworkid"))

            topworkid = int(request.POST.get("topworkid")[0])
            depid = int(request.POST.get("depid")[0])
            statuswork = request.POST.get("statuswork")

            # 将获取到的信息 进行保存个人信息

            user = models.Employee.objects.get(id=id)

            user.password = password
            user.empname = empname
            user.sex = sex
            user.birth = birth
            user.img = img
            user.nation = nation
            user.empstatus = empstatus
            user.edu = edu
            user.address = address
            user.merr = merr
            user.idcard = idcard
            user.phone = phone
            user.idAddress = idAddress
            user.idwork = idwork
            user.datework = datework
            user.postwork = postwork
            user.levelwork = levelwork
            user.topworkid = topworkid
            user.depid = depid
            user.statuswork = statuswork

            c = user.save()

            if c != 0:
                return HttpResponse("修改成功！！！")

            else:
                return HttpResponse("修改失败！！！")

    else:
        return render(request, "login.html")


def delete(request):
    uid = request.session.get("user")

    if uid  is not None:

        id = request.GET.get("id")[0]

        print(id)

        c = models.Employee.objects.get(id=id).delete()

        if c != 0:
            return HttpResponse("删除成功！！")
        else:
            return HttpResponse("删除失败！！")
    else:

        return render(request,"login.html")


def add(request):
    uid = request.session.get("user")

    if uid is not None:

        if request.method=="GET":
            return render(request, "add_employee.html")
        if request.method=="POST":

            empname = request.POST.get("empname")
            pic = request.FILES.get("pic")
            sex = request.POST.get("sex")
            birth = request.POST.get("birth")
            uid1 = request.POST.get("uid")[0]
            nation = request.POST.get("nation")
            empstatus = request.POST.get("empstatus")
            edu = request.POST.get("edu")
            address = request.POST.get("address")
            merr = request.POST.get("merr")
            idcard = request.POST.get("idcard")
            phone = request.POST.get("phone")
            idAddress = request.POST.get("idAddress")
            idwork = request.POST.get("idwork")
            datework = request.POST.get("datework")
            postwork = request.POST.get("postwork")
            levelwork = request.POST.get("levelwork")
            topworkid = request.POST.get("topworkid")[0]
            depid = request.POST.get("depid")[0]
            statuswork = request.POST.get("statuswork")

            save_path='/static/media/upload/'+pic.name

            print(save_path)

            with open(os.path.join(BASE_DIR,'static','media',pic.name),'wb') as f:

                for content in pic.chunks():
                    f.write(content)

            c = models.Employee.objects.create(empname=empname,uid=uid1,pic='media/'+pic.name,sex=sex,birth=birth,nation=nation,empstatus=empstatus,edu=edu,
                                           address=address,merr=merr,idcard=idcard,phone=phone,idAddress=idAddress,idwork=idwork,datework=datework,postwork=postwork,
                                           levelwork=levelwork,topworkid=topworkid,depid=depid,statuswork=statuswork)
            if c != 0:

                return HttpResponse("增加成功")
            else:
                return HttpResponse("增加失败！")


    else:
        return render(request,"login.html")

