from django.db import models

class Policy(models.Model):
    policy_number = models.CharField(max_length=255)
    holder_name = models.CharField(max_length=255, blank=True, default="")
    policy_type = models.CharField(max_length=50, choices=[("life", "Life"), ("health", "Health"), ("motor", "Motor"), ("property", "Property"), ("travel", "Travel")], default="life")
    premium = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    coverage = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("expired", "Expired"), ("cancelled", "Cancelled"), ("claimed", "Claimed")], default="active")
    agent = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.policy_number

class Claim(models.Model):
    claim_number = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255, blank=True, default="")
    claimant = models.CharField(max_length=255, blank=True, default="")
    claim_type = models.CharField(max_length=50, choices=[("cashless", "Cashless"), ("reimbursement", "Reimbursement")], default="cashless")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("filed", "Filed"), ("under_review", "Under Review"), ("approved", "Approved"), ("rejected", "Rejected"), ("settled", "Settled")], default="filed")
    filed_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.claim_number

class InsureCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    dob = models.DateField(null=True, blank=True)
    policies_count = models.IntegerField(default=0)
    total_premium = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    agent = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
