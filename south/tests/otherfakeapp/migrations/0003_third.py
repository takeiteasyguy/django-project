from django.db import models
from south.db import db


class Migration:
    
    depends_on = (
        ("fakeapp", "0003_alter_spam"),
    )
    
    def forwards(self):
        pass
    
    def backwards(self):
        pass
