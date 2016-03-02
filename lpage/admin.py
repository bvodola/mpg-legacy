from django.contrib import admin
from lpage.models import *

class CharFieldInline(admin.TabularInline):
	model = CharField
	extra = 1

class TextFieldInline(admin.TabularInline):
	model = TextField
	extra = 1

class IntegerFieldInline(admin.TabularInline):
	model = IntegerField
	extra = 1

class ImageFieldInline(admin.TabularInline):
	model = ImageField
	extra = 1

class CustomPageAdmin(admin.ModelAdmin):
	inlines = [
		CharFieldInline,
		TextFieldInline,
		IntegerFieldInline,
		ImageFieldInline,
	]

class ESPMCourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'starting_date', 'location', 'category', 'is_active',)
	list_editable = ('starting_date', 'location', 'category', 'is_active',)

admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(CharField)
admin.site.register(TextField)
admin.site.register(IntegerField)
admin.site.register(ImageField)
admin.site.register(GlobalData)
admin.site.register(ESPMCourse, ESPMCourseAdmin)