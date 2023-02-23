from django.apps import AppConfig
from django.db.models.signals import post_migrate
import random
from FirstApplication.models import Name, ID, Contact, Address



def populate_models(sender, **kwargs):
    from FirstApplication.models import Name, ID, Contact, Address



first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
last_names = ['Anderson', 'Brown', 'Clark', 'Davis', 'Edwards']
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
streets = ['Main St', 'Maple Ave', 'Oak St', 'Elm St', 'Cedar Rd']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
states = ['NY', 'CA', 'IL', 'TX', 'AZ']
zip_codes = ['10001', '90001', '60601', '77001', '85001']

for i in range(30):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f'{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}'
    phone_number = f'({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}'
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.choice(zip_codes)

    name = Name.objects.create(first_name=first_name, last_name=last_name)
    id = ID.objects.create(id_number=random.randint(100000, 999999))
    contact = Contact.objects.create(email=email, phone_number=phone_number)
    address = Address.objects.create(street=street, city=city, state=state, zip_code=zip_code)

    class FirstApplicationConfig(AppConfig):
     default_auto_field = 'django.db.models.BigAutoField'
     name = 'FirstApplication'

    def ready(self):
        post_migrate.connect(populate_models, sender=self)

