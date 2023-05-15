from django.contrib import admin
#
from .models import Post, Category, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''
    pass

@admin.register(Favorite)
class FavoriteyAdmin(admin.ModelAdmin):
    '''Admin View for Favorite'''
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''
    
    save_as = True
    

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
