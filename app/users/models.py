from app.users.managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'email'

    followers = models.ManyToManyField("self", blank=True, related_name='followers_user_list', symmetrical=False)
    following = models.ManyToManyField("self", blank=True, related_name='following_user_list', symmetrical=False)

    def __str__(self):
        return self.email

    def followers_list(self):
        list_of_followers = []
        for users in self.followers.all():
            list_of_followers.append(users.username)
        return len(list_of_followers)

    def following_list(self):
        list_of_following = []
        for users in self.following.all():
            list_of_following.append(users.username)
        return len(list_of_following)

class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_liked_users = models.ManyToManyField(User, blank=True, related_name='post_liked_users')

    message_text = models.TextField(blank=False, null=False)
    post_liked = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
