from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """旅行团的设置"""
    tour_name = models.CharField('旅行团名称', max_length=100)
    text = models.CharField('旅行团备注', max_length=200, null=True)
    route1 = models.CharField('行程1', max_length=200, null=True)
    route2 = models.CharField('行程2', max_length=200, null=True)
    route3 = models.CharField('行程3', max_length=200, null=True)
    route4 = models.CharField('行程4', max_length=200, null=True)
    route5 = models.CharField('行程5', max_length=200, null=True)
    date_added = models.DateField('建立时间', auto_now_add=True)
    date_start = models.DateField('出发日期')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.tour_name

    # 定义Topic模型的显示名字
    class Meta:
        verbose_name = '旅行团名称'
        # 模型的复数形式
        verbose_name_plural = '旅行团名称'
