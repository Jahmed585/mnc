from .models import Course, Lesson, Instructor, Learner
class ChoiceInline(admin.StackedInline):
		model = Choice
		extra = 2

class QuestionInline(admin.StackedInline):
		model = Question
		extra = 2
class QuestionAdmin(admin.ModelAdmin):
		inlines = [ChoiceInline]
		list_display = ['content']
  
admin.site.register(Question, QuestionAdmin)
	admin.site.register(Choice)
	admin.site.register(Submission)

