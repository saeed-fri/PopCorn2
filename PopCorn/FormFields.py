import re
from django import forms
from django.core.exceptions import ValidationError


class MyDateField(forms.Field):
    def to_python(self, value):
        match_date = re.match('^(\d{2})/(\d{2})/(\d{4})$', value)
        if match_date:
            s = value.split("/")
            return s[2]+'-'+s[1]+'-'+s[0]

    def validate(self, value):
        super(MyDateField, self).validate(value)

        match_date = re.match('^(\d{2})/(\d{2})/(\d{4})$', value)
        if not match_date:
            raise ValidationError('Date should be in DD/MM/YYYY format.', code='invalid_date')


class Password(forms.CharField):
    def validate(self, value):
        super(Password, self).validate(value)
        if len(value) < 6:
            raise ValidationError('Password must be at least 6 characters long.', code='invalid')