from django.db import models
from meido.utils.models import BaseModel
from users.models import User


# Create your models here.


class OAuthQQModel(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    openid = models.CharField(max_length=64, db_index=True)

    class Meta:
        db_table = 'tb_oauth_qq'
