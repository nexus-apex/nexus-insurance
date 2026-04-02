from django.contrib import admin
from .models import Policy, Claim, InsureCustomer

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ["policy_number", "holder_name", "policy_type", "premium", "coverage", "created_at"]
    list_filter = ["policy_type", "status"]
    search_fields = ["policy_number", "holder_name", "agent"]

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ["claim_number", "policy_number", "claimant", "claim_type", "amount", "created_at"]
    list_filter = ["claim_type", "status"]
    search_fields = ["claim_number", "policy_number", "claimant"]

@admin.register(InsureCustomer)
class InsureCustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "dob", "policies_count", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]
