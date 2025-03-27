import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Display the embedding of a randomly selected movie"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        
        if not movies.exists():
            self.stderr.write("❌ No movies found in the database.")
            return
        
        movie = random.choice(movies)
        
        embedding_array = np.frombuffer(movie.emb, dtype=np.float32)
        
        
        self.stdout.write(self.style.SUCCESS(f"🎬 Random Movie: {movie.title}"))
        self.stdout.write(f"📝 Description: {movie.description}")
        self.stdout.write(f"📊 Embedding (first 10 values): {embedding_array[:10]}")
        self.stdout.write(self.style.SUCCESS("✅ Embedding visualization completed."))
