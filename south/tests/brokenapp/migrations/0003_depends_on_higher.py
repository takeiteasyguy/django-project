from django.db import models
from south.db import db


class Migration:

    depends_on = [('brokenapp', '0004_higher')]
    
    def forwards(self):
        pass
    
    def backwards(self):
        pass

