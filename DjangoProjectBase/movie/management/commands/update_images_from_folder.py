import os
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings

class Command(BaseCommand):
    help = "Update movie images from the media folder"

    def handle(self, *args, **kwargs):
        images_folder = os.path.join(settings.MEDIA_ROOT, 'movie/images/')
        
        if not os.path.exists(images_folder):
            self.stderr.write(f"The folder '{images_folder}' does not exist.")
            return
        
        updated_count = 0
        
        for movie in Movie.objects.all():
            image_filename = f"m_{movie.title}.png"  
            image_path = os.path.join(images_folder, image_filename)
            
            if os.path.exists(image_path):
                movie.image = f"movie/images/{image_filename}" 
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))
            else:
                self.stderr.write(f"Image not found for: {movie.title}")
        
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movie images."))
