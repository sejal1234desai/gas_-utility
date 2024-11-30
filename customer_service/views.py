from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})


def success(request):
    return render(request, 'customer_service/success.html')
@login_required
def request_status(request):
    customer = request.user.customer  # Check if this returns a valid customer object
    print(f"Customer: {customer}")
    requests = ServiceRequest.objects.filter(customer=customer).order_by('-created_at')
    print(f"Requests: {requests.count()}")  
    return render(request, 'customer_service/request_status.html', {'requests': requests})
