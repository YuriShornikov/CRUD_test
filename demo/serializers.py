from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)#минимальное количество символов 10

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'create_at']

    # def validate_text(self, value):#функция для исключения
    #     if 'text' in value:
    #         raise ValidationError('использовано запрещенное слово')
    #     return value

    # def validate(self, attrs):#ограничение по нескольким значениям
    #     if 'text' in attrs['text'] or attrs['user'].id == 1:
    #         raise ValidationError('Что-то пошло не так')
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)