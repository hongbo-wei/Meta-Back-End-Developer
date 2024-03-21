from django.db import models

class Rating(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you have user authentication
    menu_item_id = models.ForeignKey('restaurant.Menu', on_delete=models.CASCADE)  # Assuming you have a Menu model
    rating = models.IntegerField()  # Assuming ratings are integers (e.g., 1 to 5 stars)

    # You might want to add additional fields such as timestamp, comments, etc.

    def __str__(self):
        return f'{self.user.username} - {self.menu_item_id.name} - Rating: {self.rating}'
