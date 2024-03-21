from django.views.generic import View
from django.http import JsonResponse
from .models import Rating

class RatingsView(View):
    def post(self, request):
        # Handle POST request to submit a rating
        data = request.POST
        # Assuming you have a model for ratings (e.g., Rating)
        rating = Rating(
            user=request.user,  # Assuming you have user authentication
            menu_item_id=data.get('menu_item_id'),
            rating=data.get('rating')
        )
        rating.save()
        return JsonResponse({'message': 'Rating submitted successfully'})

    def get(self, request):
        # Handle GET request to retrieve ratings
        # This could return a list of ratings, average ratings, etc.
        ratings = Rating.objects.all()
        # Serialize ratings and return as JSON
        # Example: ratings_json = serializers.serialize('json', ratings)
        return JsonResponse({'ratings': ratings})
