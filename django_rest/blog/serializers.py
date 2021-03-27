import email
from django.core.management.color import Style
from blog.models import Blog,Category,Tag,Comment
from rest_framework import serializers
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','comment', 'created', 'blog']

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['blog'] = instance.blog.name
        return rep

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','title']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title']



class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id',  'name', 'is_active', 'author_name','category','tag','order']

        extra_kwargs = {
            'is_active': {'read_only': True},
            'id':{"read_only":False}
        }



class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True,)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
    

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "პაროლები არ ემთხვევა"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user