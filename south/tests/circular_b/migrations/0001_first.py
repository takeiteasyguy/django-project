from django.db import models
from south.db import db


class Migration:
    
    depends_on = [('circular_a', '0001_first')]
    
    def forwards(self):
        pass
    
    def backwards(self):
        pass

