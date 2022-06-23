from django.test import TestCase
from rest_framework.test import APIClient
from .models import Firearm
from user.models import User
import datetime
from decimal import Decimal


class FirearmDatabaseTest(TestCase):
    
    def setUp(self):
        self.username = 'unitTester'
        self.password = '123abcd456'
        self.email = 'unitTester@tests.com'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )
        self.rifle, self.created = Firearm.objects.get_or_create(
            user=self.user,
            type='Rifle',
            manufacturer='Springfield Armory',
            model='M1 Garand',
            caliber='.30-06',
            serial_number='0000001',
            est_value=Decimal('1500.00'),
            date_purchased=datetime.date.today(),
            notes='Surplus M1 Garand from WW2 made at Springfield Armory, MA. Bought at the CMP.'
        )
    

    def test_firearm_database(self):
        """
        See if the firearm is in the database.
        """
        db_record = Firearm.objects.filter(user=self.user, serial_number='0000001')
        self.assertTrue(db_record)

