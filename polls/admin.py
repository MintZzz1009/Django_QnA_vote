from django.contrib import admin

# Register your models here.

from polls.models import Question, Choice


# class ChoiceInline(admin.StackedInline): # 스택 형식으로 보기
class ChoiceInline(admin.TabularInline): # 테이블 형식으로 보기
    model = Choice
    extra = 2 # 한 번에 보여주는 Choice_text 개수


# admin에서 qusetion 데이터 필드 순서변경
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'], # 필드 순서 변경
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        # 'classes': ['collapse'] -> 토글기능 추가
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date', )    # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']  # 필터 사이드 바 추가
    search_fields = ['question_text']   # 검색 박스 추가


# admin.site.register(Question) 
admin.site.register(Question, QuestionAdmin) # 2번째 인자 추가
admin.site.register(Choice)