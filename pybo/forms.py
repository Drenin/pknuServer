from django import forms
from pybo.models import Question, Answer #Question 이라는 내용을 밑의 형식에 집어 넣은 것

class QuestionForm(forms.ModelForm):#  모델과 관련된 폼이라 생각하기. 우리가 만든 모델에서 작동함
    class Meta:#  Meta 클래스라는 것은 하나의 형식. 모델 폼을 상속받을때 필요함
        model = Question
        fields = ['subject', 'content']# Question에서 가져온 'subject', 'content' 두 개를 사용한다

        labels = {
            'subject':'제목',
            'content':'내용',
        }



class AnswerForm(forms.ModelForm):#  모델과 관련된 폼이라 생각하기. 우리가 만든 모델에서 작동함
    class Meta:#  Meta 클래스라는 것은 하나의 형식. 모델 폼을 상속받을때 필요함
        model = Answer
        fields = ['content']# Question에서 가져온 'content' 두 개를 사용한다

        labels = {
            'content':'답변 내용',
        }