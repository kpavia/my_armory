from django.db import models
from user.models import User


class Firearm(models.Model):
    RIFLE = 'rifle'
    SHOTGUN = 'shotgun'
    HANDGUN = 'handgun'
    REVOLVER = 'revolver'
    MUSKET = 'musket'
    MG = 'mg'
    SMG = 'smg'
    FIREARM_TYPES = [
        (RIFLE, 'Rifle'),
        (SHOTGUN, 'Shotgun'),
        (HANDGUN, 'Handgun'),
        (REVOLVER, 'Revolver'),
        (MUSKET, 'Musket'),
        (MG, 'Machine Gun'),
        (SMG, 'Submachine Gun')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=FIREARM_TYPES)
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=32)
    caliber = models.CharField(max_length=32)
    serial_number = models.CharField(max_length=32, null=True)
    est_value = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    date_purchased = models.DateField(null=True)
    notes = models.TextField(null=True)

    
    def __str__(self):
        return f'{self.user}, {self.type}, {self.manufacturer} {self.model}, {self.caliber}'
    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['type', 'manufacturer', 'model', 'serial_number'],
                name = 'Firearm model'
            )
        ]

