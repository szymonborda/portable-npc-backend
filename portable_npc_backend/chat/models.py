from django.db import models

class ChatCharacter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="chat_character_images", null=True, blank=True)
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="chat_characters")

    def __str__(self):
        return self.name
