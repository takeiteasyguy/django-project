from django.db import models
from south.db import db


class Migration:

    depends_on = [('deps_b', '0003_b')]

    def forwards(self):
        pass
    
    def backwards(self):
        pass

