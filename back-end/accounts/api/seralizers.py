from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Profile


class RegisterSerial(serializers.Serializer):
    school = {'student':1, 'teacher':2}
    username = serializers.CharField(max_length = 30)
    password = serializers.CharField(max_length = 30)
    choices = serializers.ChoiceField(choices=school)

    # create methodu islemeden once bu func isleyir 
    # verileri temizlemek ucudur
    def to_internal_value(self, data):
        rep = super().to_internal_value(data)
        rep['choices'] = 1 if rep['choices'] == 'student' else 2
        return rep

    def create(self, validated_data):
        data = validated_data.pop('choices')
        user = User()        
        user.username = validated_data.get('username')
        user.set_password(validated_data.get('password'))
        user.save()
        Profile.objects.create(user = user, choices = data)
        return user    
        # return super().create(validated_data)

    # def save(self, **kwargs):
    #     return super().save(**kwargs)
    
# class Register(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['']