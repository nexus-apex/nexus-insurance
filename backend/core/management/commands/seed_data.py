from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Policy, Claim, InsureCustomer
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusInsurance with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusinsurance.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Policy.objects.count() == 0:
            for i in range(10):
                Policy.objects.create(
                    policy_number=f"Sample {i+1}",
                    holder_name=f"Sample Policy {i+1}",
                    policy_type=random.choice(["life", "health", "motor", "property", "travel"]),
                    premium=round(random.uniform(1000, 50000), 2),
                    coverage=round(random.uniform(1000, 50000), 2),
                    start_date=date.today() - timedelta(days=random.randint(0, 90)),
                    end_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["active", "expired", "cancelled", "claimed"]),
                    agent=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Policy records created'))

        if Claim.objects.count() == 0:
            for i in range(10):
                Claim.objects.create(
                    claim_number=f"Sample {i+1}",
                    policy_number=f"Sample {i+1}",
                    claimant=f"Sample {i+1}",
                    claim_type=random.choice(["cashless", "reimbursement"]),
                    amount=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["filed", "under_review", "approved", "rejected", "settled"]),
                    filed_date=date.today() - timedelta(days=random.randint(0, 90)),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Claim records created'))

        if InsureCustomer.objects.count() == 0:
            for i in range(10):
                InsureCustomer.objects.create(
                    name=f"Sample InsureCustomer {i+1}",
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    dob=date.today() - timedelta(days=random.randint(0, 90)),
                    policies_count=random.randint(1, 100),
                    total_premium=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "inactive"]),
                    agent=f"Sample {i+1}",
                    address=f"Sample address for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 InsureCustomer records created'))
