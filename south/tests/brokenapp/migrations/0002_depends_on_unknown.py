from django.db import models
from south.db import db


class Migration:

    depends_on = [('fakeapp', '9999_unknown')]
    
    def forwards(self):
        pass
    
    def backwards(self):
        pass

