from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from github import Github
from social_django.models import UserSocialAuth


def login(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    user = request.user
    # since we use github only
    social_user = UserSocialAuth.objects.get(user=user)
    github_token = social_user.extra_data['access_token']

    g = Github(github_token)
    github_user = g.get_user()

    repos = [repo for repo in github_user.get_repos()]
    return render(
        request,
        'profile.html',
        context={
            'reps': repos,
            'github_user': github_user
        }
    )
