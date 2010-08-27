"""
Creates the default AboutMe object.
"""

from django.db.models import signals
from aboutme.models import AboutMe
from aboutme import models as models_app

BIO = '''Sed velit ipsum, tempus id suscipit vel, eleifend vitae orci. 
Fusce molestie consequat semper. Phasellus aliquet ultricies lacus nec congue.
Proin est felis, sollicitudin eget euismod eget, tempor at neque. 
In viverra sem vitae dui cursus a feugiat tortor fermentum. 
Nunc pellentesque nisl non metus pretium sollicitudin. 
Phasellus nunc lectus, molestie ullamcorper imperdiet nec, pulvinar vel nibh. 
Sed eu nisi semper sapien aliquam interdum eget eget mauris.
Nunc in felis metus. Cum sociis natoque penatibus et magnis dis 
parturient montes, nascetur ridiculus mus. Ut mi ipsum, 
tristique eget molestie luctus, dignissim sed augue.'''


def create_default_aboutme_content(app, created_models, verbosity, db, **kwargs):
    if AboutMe in created_models:
        if verbosity >= 2:
            print "Creating default about me data"
        aboutme = AboutMe(given_name='Andriy',
                           family_name='Tomchuk',
                           middle_name='Yuriyovich',
                           cell_phone='+380638671171',
                           home_phone='+380322706966',
                           bio=BIO)
        aboutme.save()

signals.post_syncdb.connect(create_default_aboutme_content, sender=models_app)

