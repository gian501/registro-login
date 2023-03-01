from django.db import models
'''from django.contrib.auth.models import User #lo saca de aca
from django.db.models.signals import post_save # para que cuando se crea un usuario me dispare el usuario
# Create your models here.


class Profile(models.Model): #campos a guardar
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	avatar = models.ImageField(default='users/image_user.png', upload_to='users/')
	biografia = models.TextField(max_length=600, null=True, blank=True)

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
		ordering = ['-id']

def create_user_profile(sender, instance, created, **kwargs): #despues de definir las signals debo definir esto
	if created: #si se creo el usuario 
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs): #graba el profile si el usuario lo modifica  
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)#esto envia el perfil
post_save.connect(save_user_profile, sender=User) #esto lo graba'''