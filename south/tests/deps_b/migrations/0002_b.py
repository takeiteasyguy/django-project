from django.db import models
from south.db import db


class Migration:

    depends_on = [('deps_a', '0002_a')]

    def forwards(self):
        pass
    
    def backwards(self):
        pass

