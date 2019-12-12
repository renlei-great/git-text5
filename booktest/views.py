from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from booktest.models import BookInfo, Poctest, AreaInfo
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from test5 import settings


# Create your views here.
def login_requeired(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.has_key('islogin'):
            # 没有登录过
            return redirect('/login')
        else:
            # 已经登录了
            return view_func(request, *args, **kwargs)
    return wrapper



def index(request):
    # # 1.引入模板文件
    # temp = loader.get_template('booktest/index.html')
    # # 2.调用上下文管理
    # context = RequestContext(request, {})
    # # 3.对模板进行渲染
    # temp = temp.render(context)
    # # 4.进行返回
    # return HttpResponse(temp)
    return render(request, 'booktest/index.html', {})


def index2(request):
    return render(request, 'booktest/index2.html')


def login(request):
    return render(request, 'booktest/login.html')


# /temp_var
def temp_var(request):
    dict_var = {'name': 'renlei'}
    list_var = ['aa', 'bb', 'cc']
    book = BookInfo.objects.all()
    # 定义上下文
    context = {
        'dict_var': dict_var,
        'list_var': list_var,
        'books': book,
    }

    return render(request, 'booktest/temp_var.html', context)


# /temp_chide1
def temp_chide1(request):
    return render(request, 'booktest/chide1.html', {'context': '<h1> 转义 </h1>'})


def login(request):
    """登录"""


    """判断用户是否已经登录过"""
    if request.session.has_key('islogin'):
        # 访问修改密码页面
        return redirect('/change')
    else:
        # panduan
        if request.session.has_key('username') and request.session.has_key('password'):
            username = request.session.get('username')
            password = request.session.get('password')
            # request.session['islogin'] = True
        else:
            username = ''
            password = ''

        return render(request, 'booktest/login.html', {'username': username, 'password': password})


def login_chke(request):
    """判断输入的密码和用户名是否正确"""

    # 判断验证码
    xt_vcode = str(request.session.get('verifycode'))  # 获取系统生成的验证码
    yh_vcode = str(request.POST.get('vcode'))  # 获取用户的输入验证码
    print("用户%s" % yh_vcode)
    print("系统%s" % xt_vcode)
     # 进行判断是否正确
    if xt_vcode.upper() != yh_vcode.upper():
        # 错误
        return redirect('/login')


    name = request.POST.get('username')
    pwd = request.POST.get('password')
    remeber = request.POST.get('remeber')

    # 判断输入是否正确
    if name == 'admin' and pwd == '123':
        request.session['islogin'] = True
        response = render(request, 'booktest/change.html', {'username': name})
        # 判断是否需要记住用户或密码
        if remeber == 'on':
            request.session['username'] = name
            request.session['password'] = pwd
        return response
    else:
        return redirect('/login')

# /change # 修改密码页面
@login_requeired
def change(request):
    return render(request, 'booktest/change.html')


# /change_action 点击修改执行的
@login_requeired
def change_action(request):
    new_pwd = request.POST.get('password')
    username = request.session.get('username')

    return HttpResponse(str(username) +'的新密码是'+ str(new_pwd))


# /verify_code  验证码
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    img = HttpResponse(buf.getvalue(), 'image/png')
    # print(img)
    return HttpResponse(img)
    # return HttpResponse(buf.getvalue(), 'image/png')


    # /verify_code_ajax  用于ajax请求
def verify_code_ajax(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png

    # return HttpResponse(buf.getvalue(), 'image/png')
    # img = HttpResponse(buf.getvalue(), 'image/png')
    print("777")
    img = JsonResponse(buf.getvalue(), 'image/png')
    print("333")
    print(img)
    return JsonResponse({'res': str(img)})


def redirect_index(request):


    return render(request, 'booktest/redirect_index.html')


# /upload  上传图片页面
def upload(request):
    return render(request, 'booktest/upload.html')

# /upload_img  确认上传，进行图片保存
def upload_img(request):

    # 1. 获取前端送来的文件
    pic = request.FILES['file_img']

    # print(type(pic)) #for test
    # 2. 保存文件
    path = "%s/booktest/%s" % (settings.MEDIA_ROOT, pic.name)
    with open(path, 'wb') as f:
        for context in pic.chunks():
            f.write(context)
    # 3. 数据库进行记录
    Poctest.objects.create(gpic= 'booktest/%s' % pic.name)

    # 4. 返回
    return HttpResponse('OK')


def pic_show(request):
    pic = Poctest.objects.get(pk=7)
    context = {'pic':pic}
    return render(request, 'booktest/pic_show.html', context)


# /page_test  分页显示省级城市
def page_test(request, index):
    area = AreaInfo.objects.filter(aParent__isnull= True)

    # 对查询结果进行分页
    pagin = Paginator(area, 10)

    # 判断传入的index是否为空，并转为int
    if index == '':
        index = 1
    else:
        int(index)

    # 获取第一页码
    page = pagin.page(index)

    context = {'page': page }
    return render(request, 'booktest/page_test.html', context)


# / areas
def ares(request):


    return render(request, 'booktest/areas.html')


# /prov  查询省级城市
def prov(request):
    # 1. 查出所有省级城市
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 拼接查询出来的所有省级城市
    areas_list = []
    for area in areas:
        areas_list.append([area.id, area.atitle])
    # 2. 返回所有省级城市，注：jsonresrponse不能直接接受对象
    return JsonResponse({'data': areas_list})


# /city  查询省下的所有市
def city(request, pro_id):
    # 1. 查询这个省下的所有市
    areas = AreaInfo.objects.filter(aParent= pro_id)

    # 2. 将查出来的数据进行拼接成列表
    area_list = []
    for area in areas:
        id = area.id
        atitle = area.atitle

        area_list.append((id, atitle))

    # 3. 返回给ajax
    return JsonResponse({'data': area_list})


# # /county  市下的所有县
# def county(request, coun_id):
#     # 查询出这个市下的所有县
#     areas = AreaInfo.objects.filter(aParent=coun_id)
#
#     # 将areas对象中的所有县装到列表中
#     area_list = []
#     for area in areas:
#         id = area.id
#         atitle = area.atitle
#
#         area_list.append((id, atitle))
#
#     # 将列表返回给前端
#     return JsonResponse({'data': area_list})


def jiade(request):
    pass