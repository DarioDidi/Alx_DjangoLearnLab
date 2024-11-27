from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        curr_yr = datetime.now().year
        if curr_yr < data['publication_year']:
            raise serializers.ValidationError("Year cannot be in the future")


class AuthorSerializer(serializers.ModelSerializer):
    BookSerializer = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('name',)
