"""
Creates the default AboutMe object.
"""

from django.db.models import signals
from aboutme.models import AboutMe
from aboutme import models as models_app

def create_default_aboutme_content(app, created_models, verbosity, db, **kwargs):
    if AboutMe in created_models:
        if verbosity >= 2:
            print "Creating default about me data"
        s = AboutMe(name="first_name", title="First name", description="Andriy")
        s.save(using=db)
        s = AboutMe(name="family_name", title="Family name", description="Tomchuk")
        s.save(using=db)
        s = AboutMe(name="middle_name", title="Middle name", description="Yurirovich")
        s.save(using=db)
        s = AboutMe(name="cell_phone", title="Cell phone", description="+380638671171")
        s.save(using=db)
        s = AboutMe(name="home_phone", title="Home phone", description="+380638671171")
        s.save(using=db)

signals.post_syncdb.connect(create_default_aboutme_content, sender=models_app)

