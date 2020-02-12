from django.db import models

# Create your models here.

# 管理员表（Sup_user）
# 管理员账号（char）
# 管理员昵称（char）
# 登录密码（char）
class Administrators(models.Model):
    administrator_id = models.CharField(max_length=30, null=False, verbose_name='账户_id')
    administrator_name = models.CharField(max_length=30, default='root', null=False, verbose_name='用户昵称')
    administrator_pwd = models.CharField(max_length=100, null=False, verbose_name='用户密码')
    administrator_jifen = models.DecimalField(max_digits=4, decimal_places=2, default=1, verbose_name='积分')
    administrator_email = models.CharField(max_length=100, null=False, verbose_name='用户邮箱', default="123@163.com")

    def __str__(self):
        return str(self.administrator_id)

    class Meta:
        db_table = 'super_user'
        verbose_name = '管理员信息'
        verbose_name_plural = verbose_name

# 购买人年龄段
AGES_CHOICES = (
    ('a', '<19'),
    ('b', '20-35'),
    ('c', '36-55'),
    ('d', '>55'),
    ('e', '不确定'),
)

# 购买人性别
SEX_CHOICES = (
    ('a', '男'),
    ('b', '女'),
)

# 购买人表
class Buy_peoples(models.Model):
    administrator_id = models.ForeignKey(Administrators, on_delete=models.CASCADE, verbose_name='管理员账户_id')
    buy_people_name = models.CharField(max_length=50, null=False, verbose_name='购买人姓名')
    buy_people_alljifen = models.DecimalField(max_digits=10,decimal_places=2, default=0, verbose_name='总积分')
    buy_people_keyongjifen = models.DecimalField(max_digits=10,decimal_places=2, default=0, verbose_name='可用积分')
    buy_people_allmoney = models.DecimalField(max_digits=10,decimal_places=2, default=0, verbose_name='总消费金额 ')
    buy_people_phone = models.CharField(max_length=11, default='18888888888', verbose_name='购买人手机号')
    buy_people_addr = models.TextField(default='暂无', verbose_name='购买人地址')
    buy_people_age = models.CharField(max_length=20, default=2, choices=AGES_CHOICES, verbose_name='购买人年龄')
    buy_people_sex = models.CharField(max_length=20, default=1, choices=SEX_CHOICES, verbose_name='购买人性别')
    # is_show为True即为删除
    buy_people_is_show = models.BooleanField(default=True, verbose_name='是否显示')

    def __str__(self):
        return str(self.buy_people_name)

    class Meta:
        db_table = 'buy_peoples'
        verbose_name = '购买人信息'
        verbose_name_plural = verbose_name


# 类别
# Sup_user(F.Sup_user)
# 商品类别（char）
class Goods_types(models.Model):
    administrator_id = models.ForeignKey(Administrators, on_delete=models.CASCADE, verbose_name='管理员账户_id')
    leibie_id = models.CharField(max_length=20, default='LB0001', verbose_name='类别编码')
    leixing = models.CharField(max_length=50, verbose_name='类别名称')
    jibie = models.CharField(max_length=15, verbose_name='级别', default='一级')

    def __str__(self):
        return str(self.leixing)

    class Meta:
        db_table = 'goods_types'
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name
# 商品表
# 商品类别（F.类别）
# 商品编号（char）
# 商品名称（char）
# 商品价格（Int）
class Goods(models.Model):
    administrator_id = models.ForeignKey(Administrators, on_delete=models.CASCADE, verbose_name='管理员账户_id')
    goods_id = models.CharField(max_length=50, null=False, verbose_name='商品编号')
    goods_name = models.CharField(max_length=50, null=False, default='无名氏', verbose_name='商品名称')
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    goods_type = models.ForeignKey(Goods_types, on_delete=models.CASCADE, verbose_name='商品类别')
    goods_kucun = models.IntegerField(default=0, verbose_name='库存')
    goods_xiaoliang = models.IntegerField(default=0, verbose_name='销量')
    goods_text = models.TextField(default='暂无描述', verbose_name='商品描述')
    goods_guige = models.CharField(max_length=100, default='无', verbose_name='商品规格')
    goods_jifen = models.DecimalField(max_digits=7, decimal_places=2, default=100.00, verbose_name='兑换所需积分')
    # goods_is_duiuan = models.BooleanField(default=False, verbose_name='是否可以兑换')

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
# 订单表
# 订单编号
# 购买人姓名（F.购买人表）
# 购买人编号
# 商品名称
# 商品价格
# 商品类别（F.类别）
# 获得积分
# 订单生成时间
import datetime

# 生成订单编号
def bianhao():
    bianhao = str(datetime.datetime.now())
    bianhao = bianhao.split()
    bianhao1 = bianhao[0].split('-')
    bianhao2 = bianhao[1].split(':')
    bianhao3 = bianhao2[2].split('.')
    bianhao = bianhao1+bianhao2[0:2]+bianhao3
    x = ''
    for i in bianhao:
        x+=i
    return x

# 购买方式
PAY_CHOICES = (
    ('a', '现金'),
    ('b', '刷卡'),
    ('c', '支付宝'),
    ('d', '微信'),
    ('e', '积分兑换'),

)

now_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

class Order(models.Model):
    administrator_id = models.ForeignKey(Administrators, default=1, on_delete=models.CASCADE, verbose_name='管理员账户_id')
    order_id = models.CharField(max_length=50, default=bianhao(),
                                null=False, verbose_name='订单编号')
    buy_prople = models.ForeignKey(Buy_peoples, verbose_name='购买人')
    # goods = models.ManyToManyField(Goods, verbose_name='商品', default=1)
    dingdanshijian = models.DateTimeField(verbose_name='订单时间', auto_now_add=True)
    chengjiao_money = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='优惠前金额')
    chengjiao_allmoney = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='优惠后金额')
    youhuijine = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='优惠金额')
    goumailiang = models.IntegerField(verbose_name='购买量', default=0)
    huodejifen = models.DecimalField(max_digits=7, decimal_places=2,default=0, verbose_name='获得积分')
    zhifufangshi = models.CharField(max_length=20, default=2, choices=PAY_CHOICES, verbose_name='支付方式')
    xiaohaojifen = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='消耗积分')
    # order_is_show 为True即为删除
    order_is_show = models.BooleanField(default=True, verbose_name='是否显示')

    def __str__(self):
        return str(self.order_id)


    class Meta:
        db_table = 'orders'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

class Cart(models.Model):
    goods_id = models.ForeignKey(Goods, verbose_name='商品信息', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, verbose_name='订单信息', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='购买数量')

    def __str__(self):
        return str(self.goods_id)


    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

