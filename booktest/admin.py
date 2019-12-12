from django.contrib import admin
from booktest.models import BookInfo, AreaInfo, Poctest


# Register your models here.

class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    # 额外可以编辑的对象
    extra = 2  # 额外可以编辑两个对象


class BookInfoAdmin(admin.ModelAdmin):
    """图书管理类"""
    list_display = ['book_name', 'book_date', 'bread']
    list_per_page = 1
    actions_on_bottom = True
    actions_on_top = False


class AreaInfoAdmin(admin.ModelAdmin):
    """地区管理类"""
    list_per_page = 10
    list_display = ['id', 'atitle', 'title', 'parent']
    search_fields = ['atitle']

    # 编辑页的调整
    # fields = ['aParent', 'atitle']  # 调整谁在上谁在下
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )  # 对显示内容进行分组显示

    inlines = [AreaStackedInline]



admin.site.register(Poctest)
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)
