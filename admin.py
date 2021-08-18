from django.contrib import admin
from .models import Core_team,Media,Product,Core_services,Other_services,Office_mail,Business_hours,Office_address,Official_telephone_number,Carosue,Index_writeup,Vision_mission,Quote,Stats,Services,Projects,Category,Blog,Comment,About,Our_clients,Productlist,CategoryP,ShopProduct

# Register your models here.
admin.site.register(Carosue)
admin.site.register(Index_writeup)
admin.site.register(Vision_mission)
admin.site.register(Quote)
admin.site.register(Stats)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(Productlist)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',)}
    
admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)

admin.site.register(About)
admin.site.register(Our_clients)
admin.site.register(Business_hours)
admin.site.register(Office_address)
admin.site.register(Office_mail)
admin.site.register(Official_telephone_number)
admin.site.register(Core_services)
admin.site.register(Core_team)
admin.site.register(Other_services)

class CategoryPAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CategoryP, CategoryPAdmin)


class ShopProductAdmin(admin.ModelAdmin):
    list_display = ['product_name1', 'slug', 'product_price1', 'available']
    list_filter = ['available']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('product_name1',)}


admin.site.register(ShopProduct, ShopProductAdmin)
