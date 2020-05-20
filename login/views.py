
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from employee import models
from login.models import Department
from employee.models import Employee
from login.models import User


def login(request):

    role = request.session.get("role")
    uid = request.session.get("user")

    if role is not None:
        if role == "1":  # 查询管理员所需要的用户信息

            employees = Employee.objects.all()

            departments = Department.objects.all()

            return render(request, "admin.html", {'es': employees, "ds": departments})

        else:



            employee = models.Employee.objects.get(uid=uid)

            if employee is  not None:

                return render(request, "employee.html", {'e': employee})
            else:

                return HttpResponse("暂时没有信息")

    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:

            if User.objects.filter(username=username, password=password) is not None:

                user = User.objects.get(username=username, password=password)

                print("hhhhhhhhhh" + user.role)

                if user is not None:

                    request.session['user'] = user.id
                    request.session['role'] = user.role

                    if user.role == "1":  # 查询管理员所需要的用户信息

                        employees = Employee.objects.all()

                        departments = Department.objects.all()

                        return render(request, "admin.html", {'es': employees, "ds": departments})

                    else:

                        employee = models.Employee.objects.get(uid=user.id)
                        if employee is not None:

                            return render(request, "employee.html", {'e': employee})
                        else:

                            return HttpResponse("暂时没有信息")
                else:
                    return HttpResponse("账户登录失败")
            else:

                return HttpResponse("账户密码错误")

        else:
            return HttpResponse("请输入账号密码！！")