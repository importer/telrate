from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Person(models.Model):
    """docstring for Person"""
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Useraccount(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    phone = models.CharField(max_length=13, blank=True, verbose_name="手机号码")
    device = models.CharField(max_length=50, blank=True, verbose_name="imei号")


class Meta(AbstractUser.Meta):
    swappable = 'AUTH_USER_MODEL'


class TypeInfo(models.Model):  # index首页商品分类信息
    ttitle = models.CharField('类型名称', max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)  # 是否删除,默认不删

    def __str__(self):
        return self.ttitle

    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'


class GoodsInfo(models.Model):  # 商品信息
    title = models.CharField('商品名称', max_length=20)
    pic = models.ImageField('商品图片', upload_to='df_goods', null=True, blank=True)  # 商品图片
    address = models.CharField('商品地址', max_length=20)  # 商品地址
    position = models.CharField('经纬度', max_length=20)  # 经纬度
    movie_name = models.CharField('电影名', max_length=20)  # 电影名
    Cinema = models.CharField('电影院名', max_length=20)  # 电影院
    seat = models.CharField('座位信息', max_length=20)  # 座位信息
    redeem_code = models.CharField('兑换码', max_length=20)  # 座位信息
    code_sms = models.CharField('买票短信', max_length=500)  # 商品的单位
    price = models.DecimalField('票价', max_digits=7, decimal_places=2)  # 总共最多有7位,小数占2位
    amount = models.IntegerField('数量')  # 商品库存
    startDate = models.DateTimeField('开始时间', auto_now=True)  # 开始时间
    endDate = models.DateTimeField('结束时间', max_length=20)  # 结束时间
    gclick = models.IntegerField('点击量')  # 商品点击量,便于排人气
    state = models.BooleanField('状态', default=True)
    remark = models.CharField('备注', max_length=200)  # 备注
    gtype = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)  # 商品所属类型

    # gadv = models.BooleanField(default=False)   #商品推荐
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'


class Accounts(models.Model):
    use_id = models.ForeignKey(Useraccount, verbose_name='用户id', on_delete=models.CASCADE)  # 用户
    amount = models.DecimalField('余额', max_digits=7, decimal_places=2)
    Coin = models.DecimalField('金币数量', max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = '账户信息'
        verbose_name_plural = '账户信息'
