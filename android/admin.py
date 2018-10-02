from django.contrib import admin
from android.models import Person, Useraccount, GoodsInfo, TypeInfo, Accounts


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password')


@admin.register(Useraccount)
class UseraccountAdmin(admin.ModelAdmin):
    # list_display=('id', 'name', 'password')  
    pass


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie_name', 'amount', 'Cinema', 'endDate', 'state')
    list_filter = ('endDate', 'state')
    search_fields = ('title', 'Cinema', 'movie_name')


@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ttitle', 'isDelete')


@admin.register(Accounts)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ('use_id', 'amount', 'Coin')
