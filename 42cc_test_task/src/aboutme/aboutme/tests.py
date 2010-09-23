from django.test import TestCase
from django.contrib.auth.models import User

from aboutme.models import AboutMe

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

class AppTestCase(TestCase):
    """
    Populate this class with unit tests for your application
    """
    
    urls = 'aboutme.test_urls'

    
    @classmethod
    def testCreateFixture(cls):
        """
        This method is used as one to create fixture for initial data
        """

        aboutme = AboutMe(given_name='Andriy',
                            family_name='Tomchuk',
                            middle_name='Yuriyovich',
                            cell_phone='+380638671171',
                            home_phone='+380322706966',
                            bio=BIO)

        
    def testIndexPage(self):
        """
        Testing index page
        """

        response = self.client.get('/aboutme/')
        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

    def testEditPage(self):
        """
        Testing edit page
        """

        user = User.objects.create_user('bob', 'marley@thewailers.com', 'jah')
        user.is_superuser = True
        user.save()
        self.client.login(username='bob', password='jah')
        response = self.client.post('/aboutme/edit',{'given_name': 'First', 
                                                     'family_name': 'Tomchuk', 
                                                     'middle_name': 'Some Name', 
                                                     'cell_phone': '+38887777778', 
                                                     'bio': 'test'})
        aboutme = AboutMe.get_aboutme()
       
        self.assertEqual(response.status_code, 200)
        self.failUnless('Edit aboutme data.' in response.content)
        self.assertEquals(aboutme.given_name, 'First')



