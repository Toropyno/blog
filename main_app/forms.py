from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super().save(request)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return user
