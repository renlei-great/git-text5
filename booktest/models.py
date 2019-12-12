from django.db import models


# Create your models here.


class BookInfo(models.Model):
    '''图书模板'''
    # # 图书名
    # book_name = models.CharField( max_length=20)
    # # 出版日期
    # book_date = models.DateField(auto_now_add=True)
    # # 阅读量
    # bread = models.IntegerField(default=0)
    # # 评论量
    # bcomment = models.IntegerField(default=0)
    # # 删除标记
    # isDelete = models.BooleanField(default=False)

    book_name = models.CharField(max_length=30)
    # 出版日期
    book_date = models.DateField()
    # 阅读量
    bread = models.CharField(max_length=20)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField()

    class Meta:
        db_table = 'bookinfo'  # 指定模型对应的表的表名

    def __str__(self):
        return self.book_name


class AreaInfo(models.Model):
    atitle = models.CharField('恩纳', max_length=20)
    aParent = models.ForeignKey('self')

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle

    parent.short_description = '父级名称'
    title.short_description = '区域名称'
    title.admin_order_field = 'atitle'



class Poctest(models.Model):
    """上传图片模板"""
    gpic = models.ImageField(upload_to='booktest')  # 指定上传路径






















