from django.core.exceptions import ValidationError


def validate_author_email(email):
    if '@' in email:
        return email
    else:
        raise ValidationError('Not a Valid Email')