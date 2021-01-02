from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        label='제목',
        help_text='제목은 255자 이내로 작성하세요', 
        widget=forms.TextInput(
            attrs={
            'class': 'user-input',
            'placeholder': '제목을 입력하세요',
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        help_text='내용을 자유롭게 작성해주세요',
        widget=forms.Textarea(
            attrs={
                'row': 7, 
                'col': 50
            }
        ), 
    )
    
    class Meta:
        model = Article
        # 유저로부터 입력받을 항목은 제목과 내용 두개!
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        label='댓글 제목', 
        help_text='댓글은 255자 이내로 작성하세요',
        widget=forms.TextInput(
            attrs={
                'class': 'user-comment',
                'placeholder': '댓글을 입력하세요',
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ['title']