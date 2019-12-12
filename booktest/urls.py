from django.conf.urls import include, url

from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index2$', views.index2, name='index'),
    url(r'^login$', views.login),

    url(r'^temp_var$', views.temp_var),

    # 继承模板
    url(r'^temp_chide1$', views.temp_chide1),  # 继承模板一

    # 登录
    url(r'^login$', views.login), #登录页面
    url(r'^login_chke$', views.login_chke),
    url(r'^change$', views.change),
    url(r'^change_action$',views.change_action), #  修改密码


    url(r'^verify_code$', views.verify_code),  # 请求验证码

    url(r'^redirect_index$', views.redirect_index),

    url(r'^verify_code_ajax$', views.verify_code_ajax),

    url(r'^upload$', views.upload),  # 请求上传图片页面
    url(r'^upload_img$', views.upload_img),  # 上传

    url(r'^pic_show$', views.pic_show),  # 显示图片

    url(r'^page_test(\w*)$', views.page_test),

    url(r'^areas$', views.ares),  # 划分省市
    url(r'^prov$', views.prov),  # 所有省级城市
    # url(r'^city(?P<por_id>\w+)$', views.city),  # 这个省下的市
    url(r'^city(\w+)$', views.city),  # 这个省下的市
    #url(r'^county(\w+)$', views.county),  # 市下的所有县


]
