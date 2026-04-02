import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Policy, Claim, InsureCustomer


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['policy_count'] = Policy.objects.count()
    ctx['policy_life'] = Policy.objects.filter(policy_type='life').count()
    ctx['policy_health'] = Policy.objects.filter(policy_type='health').count()
    ctx['policy_motor'] = Policy.objects.filter(policy_type='motor').count()
    ctx['policy_total_premium'] = Policy.objects.aggregate(t=Sum('premium'))['t'] or 0
    ctx['claim_count'] = Claim.objects.count()
    ctx['claim_cashless'] = Claim.objects.filter(claim_type='cashless').count()
    ctx['claim_reimbursement'] = Claim.objects.filter(claim_type='reimbursement').count()
    ctx['claim_total_amount'] = Claim.objects.aggregate(t=Sum('amount'))['t'] or 0
    ctx['insurecustomer_count'] = InsureCustomer.objects.count()
    ctx['insurecustomer_active'] = InsureCustomer.objects.filter(status='active').count()
    ctx['insurecustomer_inactive'] = InsureCustomer.objects.filter(status='inactive').count()
    ctx['insurecustomer_total_total_premium'] = InsureCustomer.objects.aggregate(t=Sum('total_premium'))['t'] or 0
    ctx['recent'] = Policy.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def policy_list(request):
    qs = Policy.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(policy_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(policy_type=status_filter)
    return render(request, 'policy_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def policy_create(request):
    if request.method == 'POST':
        obj = Policy()
        obj.policy_number = request.POST.get('policy_number', '')
        obj.holder_name = request.POST.get('holder_name', '')
        obj.policy_type = request.POST.get('policy_type', '')
        obj.premium = request.POST.get('premium') or 0
        obj.coverage = request.POST.get('coverage') or 0
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.status = request.POST.get('status', '')
        obj.agent = request.POST.get('agent', '')
        obj.save()
        return redirect('/policies/')
    return render(request, 'policy_form.html', {'editing': False})


@login_required
def policy_edit(request, pk):
    obj = get_object_or_404(Policy, pk=pk)
    if request.method == 'POST':
        obj.policy_number = request.POST.get('policy_number', '')
        obj.holder_name = request.POST.get('holder_name', '')
        obj.policy_type = request.POST.get('policy_type', '')
        obj.premium = request.POST.get('premium') or 0
        obj.coverage = request.POST.get('coverage') or 0
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.status = request.POST.get('status', '')
        obj.agent = request.POST.get('agent', '')
        obj.save()
        return redirect('/policies/')
    return render(request, 'policy_form.html', {'record': obj, 'editing': True})


@login_required
def policy_delete(request, pk):
    obj = get_object_or_404(Policy, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/policies/')


@login_required
def claim_list(request):
    qs = Claim.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(claim_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(claim_type=status_filter)
    return render(request, 'claim_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def claim_create(request):
    if request.method == 'POST':
        obj = Claim()
        obj.claim_number = request.POST.get('claim_number', '')
        obj.policy_number = request.POST.get('policy_number', '')
        obj.claimant = request.POST.get('claimant', '')
        obj.claim_type = request.POST.get('claim_type', '')
        obj.amount = request.POST.get('amount') or 0
        obj.status = request.POST.get('status', '')
        obj.filed_date = request.POST.get('filed_date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/claims/')
    return render(request, 'claim_form.html', {'editing': False})


@login_required
def claim_edit(request, pk):
    obj = get_object_or_404(Claim, pk=pk)
    if request.method == 'POST':
        obj.claim_number = request.POST.get('claim_number', '')
        obj.policy_number = request.POST.get('policy_number', '')
        obj.claimant = request.POST.get('claimant', '')
        obj.claim_type = request.POST.get('claim_type', '')
        obj.amount = request.POST.get('amount') or 0
        obj.status = request.POST.get('status', '')
        obj.filed_date = request.POST.get('filed_date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/claims/')
    return render(request, 'claim_form.html', {'record': obj, 'editing': True})


@login_required
def claim_delete(request, pk):
    obj = get_object_or_404(Claim, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/claims/')


@login_required
def insurecustomer_list(request):
    qs = InsureCustomer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'insurecustomer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def insurecustomer_create(request):
    if request.method == 'POST':
        obj = InsureCustomer()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.dob = request.POST.get('dob') or None
        obj.policies_count = request.POST.get('policies_count') or 0
        obj.total_premium = request.POST.get('total_premium') or 0
        obj.status = request.POST.get('status', '')
        obj.agent = request.POST.get('agent', '')
        obj.address = request.POST.get('address', '')
        obj.save()
        return redirect('/insurecustomers/')
    return render(request, 'insurecustomer_form.html', {'editing': False})


@login_required
def insurecustomer_edit(request, pk):
    obj = get_object_or_404(InsureCustomer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.dob = request.POST.get('dob') or None
        obj.policies_count = request.POST.get('policies_count') or 0
        obj.total_premium = request.POST.get('total_premium') or 0
        obj.status = request.POST.get('status', '')
        obj.agent = request.POST.get('agent', '')
        obj.address = request.POST.get('address', '')
        obj.save()
        return redirect('/insurecustomers/')
    return render(request, 'insurecustomer_form.html', {'record': obj, 'editing': True})


@login_required
def insurecustomer_delete(request, pk):
    obj = get_object_or_404(InsureCustomer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/insurecustomers/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['policy_count'] = Policy.objects.count()
    data['claim_count'] = Claim.objects.count()
    data['insurecustomer_count'] = InsureCustomer.objects.count()
    return JsonResponse(data)
