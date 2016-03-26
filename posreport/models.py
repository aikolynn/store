#coding=utf-8
from django.db import models

# Create your models here.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class InClass(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True,verbose_name='分类名')
    isend = models.IntegerField(blank=True, null=True,verbose_name='是否末级')
    depth = models.IntegerField(blank=True, null=True,verbose_name='级数')
    idfather = models.IntegerField(blank=True, null=True,verbose_name='上级ID')
    class Meta:
        managed = False
        verbose_name='存货分类'
        verbose_name_plural=verbose_name
        db_table = 'class'
    def __unicode__(self):
        return self.name

class employee(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name='姓名')
    class Meta:
        managed = False
        verbose_name='导购'
        verbose_name_plural=verbose_name
        db_table = 'employee'
    def __unicode__(self):
        return self.name

class inventoryclass(models.Model):
    id = models.CharField(primary_key=True, max_length=255,verbose_name='ID')
    code = models.CharField(max_length=255, blank=True, null=True,verbose_name='编码')
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name='分类名称')
    isendnode = models.CharField(db_column='isEndNode', max_length=255, blank=True, null=True,verbose_name='末级标识')  # Field name made lowercase.
    depth = models.CharField(max_length=255, blank=True, null=True,verbose_name='分类级数')
    idparent = models.CharField(max_length=255, blank=True, null=True,verbose_name='上级ID')

    class Meta:
        managed = False
        verbose_name='存货分类'
        verbose_name_plural=verbose_name
        db_table = 'inventoryclass'
    def __unicode__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name=u'店铺')

    class Meta:
        managed = False
        verbose_name=u'店铺'
        verbose_name_plural=verbose_name
        db_table = 'store'
    def __unicode__(self):
       return self.name

class OrderMain(models.Model):
    order_id = models.CharField(max_length=200, blank=True, null=True,verbose_name='销售单号')
    order_data = models.DateField(blank=True, null=True,verbose_name='单据时间')
    order_weekday = models.CharField(max_length=200, blank=True, null=True,verbose_name='单据星期')
    order_saleamount = models.FloatField(blank=True, null=True,verbose_name='单据销售金额')
    order_amount = models.FloatField(blank=True, null=True,verbose_name='单据零售金额')
    idstore = models.ForeignKey('Store', db_column='idstore', blank=True, null=True,verbose_name='店铺ID')
    idemployee = models.ForeignKey(employee, db_column='idemployee', blank=True, null=True,verbose_name='导购ID')

    class Meta:
        managed = False
        verbose_name='销售主表'
        verbose_name_plural=verbose_name
        db_table = 'order_main'
    def __unicode__(self):
        return u'%s %s %s' %(self.order_id,self.order_saleamount,self.order_weekday)


class order_flow(models.Model):
    inventory_code = models.CharField(max_length=200, blank=True, null=True,verbose_name=u'存货编码')
    inventory_name = models.CharField(max_length=200, blank=True, null=True,verbose_name=u'存货名称')
    quantity = models.IntegerField(blank=True, null=True,verbose_name=u'数量')
    saleprice = models.FloatField(blank=True, null=True,verbose_name=u'销售价')
    retailprice = models.FloatField(blank=True, null=True,verbose_name=u'零售价')
    unitname=models.CharField(max_length=20,blank=True,null=True,verbose_name=u"单位")
    id_order = models.ForeignKey('OrderMain', db_column='id_order', blank=True, null=True,verbose_name=u'销售单号ID')
    id_class = models.ForeignKey(InClass, db_column='id_class', blank=True, null=True,verbose_name=u'分类ID')
    class Meta:
        managed = False
        verbose_name=u'销售流水'
        verbose_name_plural=verbose_name
        db_table = 'order_flow'
    def __unicode__(self):
        return u'%s %s' %(self.inventory_code,self.inventory_name)





