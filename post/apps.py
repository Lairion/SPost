from django.apps import AppConfig
from django.apps import apps
# import secretballot
class PostConfig(AppConfig):
    name = 'post'
    # def ready(self):
    # 	post_model = apps.get_model(self.name,"Post")
    # 	secretballot.enable_voting_on(post_model)