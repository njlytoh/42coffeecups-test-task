from django.test import TestCase

from aboutme.models import AboutMe

class AppTestCase(TestCase):
    """
    Populate this class with unit tests for your application
    """
    
    urls = 'AboutMe.test_urls'
    
    @classmethod
    def testCreateFixture(cls):
        """
        This method is used as one to create fixture for initial data
        """

        name = AboutMe(name='name', title='Given name', description='Andriy')
        name.save()

        family_name = AboutMe(name='family_name', 
                         title='Family name', 
                         description='Tomchuk')
        family_name.save()

        cell_phone = AboutMe(name="cell_phone",
                        title="Cell phone",
                        description="+380638671171")
        cell_phone.save()

        home_phone = AboutMe(name="home_phone",
                                title="Home Phone",
                                description="+380322706966")
        home_phone.save()


        
