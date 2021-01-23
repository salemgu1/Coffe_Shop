import operator
from datetime import date, timedelta

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms, models


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    movies = models.Movie.objects.all()
    return render(request, 'multiplex/index.html', {'movies': movies})


# for showing signup/login button for ADMIN(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'multiplex/customersignup.html', context=mydict)


# for checking user customer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    else:
        return redirect('admin-dashboard')


# ============================================================================================
# ADMIN RELATED views start
# ============================================================================================
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict = {
        'total_customer': models.Customer.objects.all().count(),
        'total_movie': models.Movie.objects.all().count(),
        'total_booking': models.Booking.objects.all().count(),

    }
    return render(request, 'multiplex/admin_dashboard.html', context=dict)


@login_required(login_url='adminlogin')
def admin_movie_view(request):
    return render(request, 'multiplex/admin_movie.html')


@login_required(login_url='adminlogin')
def admin_add_movie_view(request):
    if request.method == 'POST':

        movie = models.Movie()
        movie.name = request.POST['name']
        movie.actor = request.POST['actorname']
        movie.director = request.POST['directorname']
        movie.description = request.POST['description']
        movie.release_date = request.POST['release_date']
        movie.out_date = request.POST['out_date']
        movie.poster = request.FILES['poster']
        movie.video = request.POST['video']
        movie.limitation = request.POST['limitation']
        movie.hall = request.POST['hall']
        movie.hall = request.POST['org_price']
        movie.hall = request.POST['price']
        movie.save()
        start_date = request.POST['release_date']
        start_date = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
        end_date = request.POST['out_date']
        end_date = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))
        delta = timedelta(days=1)
        moviex = models.Movie.objects.get(id=movie.id)
        while start_date <= end_date:
            seat = models.Seat(movie=moviex, date=start_date)
            seat.save()
            start_date += delta
        return HttpResponseRedirect('admin-movie')
    return render(request, 'multiplex/admin_add_movie.html')


@login_required(login_url='adminlogin')
def admin_customer_view(request):
    return render(request, 'multiplex/admin_customer.html')


@login_required(login_url='adminlogin')
def admin_view_customer_view(request):
    customers = models.Customer.objects.all()
    return render(request, 'multiplex/admin_view_customer.html', {'customers': customers})


@login_required(login_url='adminlogin')
def delete_customer_view(request, pk):
    customer = models.Customer.objects.get(id=pk)
    user = models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/admin-view-customer')


@login_required(login_url='adminlogin')
def admin_add_customer_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-view-customer')
    return render(request, 'multiplex/admin_add_customer.html', context=mydict)


@login_required(login_url='adminlogin')
def admin_view_customer_booking_view(request):
    bookings = models.Booking.objects.all()
    return render(request, 'multiplex/admin_view_customer_booking.html', {'bookings': bookings})


@login_required(login_url='adminlogin')
def delete_booking_view(request, pk):
    booking = models.Booking.objects.get(id=pk)
    booking.delete()
    return HttpResponseRedirect('/admin-view-customer-booking')


def cancel_ticket_view(request, pk):
    booking = models.Booking.objects.get(id=pk)
    booking.delete()
    return HttpResponseRedirect('/customer-ticket')


@login_required(login_url='adminlogin')
def admin_view_movie_view(request):
    movies = models.Movie.objects.all()
    return render(request, 'multiplex/admin_view_movie.html', {'movies': movies})


@login_required(login_url='adminlogin')
def delete_movie_view(request, pk):
    movie = models.Movie.objects.get(id=pk)
    movie.delete()
    return HttpResponseRedirect('/admin-view-movie')


@login_required(login_url='adminlogin')
def admin_feedback_view(request):
    feedback = models.Feedback.objects.all().order_by('-id')
    return render(request, 'multiplex/admin_feedback.html', {'feedback': feedback})


# ============================================================================================
# ADMIN RELATED views end
# ============================================================================================


# ============================================================================================
# CUSTOMER RELATED views start
# ============================================================================================
@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    bookings = models.Booking.objects.filter(customer=customer).order_by('-id')
    dict = {}
    for booking in bookings:
        dict = {
            'customer': customer,
            'movieName': booking.movie,
            'seatNumber': booking.seatNumber,
            'cost': booking.cost,
            'movieDate': booking.date,
        }
        break
    return render(request, 'multiplex/customer_dashboard.html', context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request, order_by=None):
    customer = models.Customer.objects.get(user_id=request.user.id)
    movies = models.Movie.objects.all()
    if order_by:
        movies = sorted(movies, key=operator.attrgetter(order_by))
    dict = {
        'customer': customer,
        'movies': movies,
    }
    return render(request, 'multiplex/customer_home.html', context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def view_movie_details_view(request, pk):
    movie = models.Movie.objects.get(id=pk)
    dict = {
        'movie': movie,
        'customer': models.Customer.objects.get(user_id=request.user.id)
    }
    return render(request, 'multiplex/view_movie_details.html', context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    return render(request, 'multiplex/customer_profile.html', {'customer': customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_customer_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    user = models.User.objects.get(id=customer.user_id)
    userForm = forms.CustomerUserForm(instance=user)
    customerForm = forms.CustomerForm(request.FILES, instance=customer)
    mydict = {'userForm': userForm, 'customerForm': customerForm, 'customer': customer}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST, instance=user)
        customerForm = forms.CustomerForm(request.POST, instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('customer-profile')
    return render(request, 'multiplex/edit_customer_profile.html', context=mydict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def book_now_view(request, pk):
    movie = models.Movie.objects.get(id=pk)
    release_date = movie.release_date
    out_date = movie.out_date
    customer = models.Customer.objects.get(user_id=request.user.id)
    dict = {
        'release_date': str(release_date),
        'out_date': str(out_date),
        'movie': movie,
        'customer': customer,
    }
    if request.method == 'POST':
        booking_date = request.POST['booking_date']
        seats = models.Seat.objects.get(movie=movie, date=booking_date)
        setattr(movie, "popularity", getattr(movie, "popularity") + 1)
        movie.save()
        request.session['movie_id'] = movie.id
        request.session['seat_id'] = seats.id
        return HttpResponseRedirect('/choose-seat')

    return render(request, 'multiplex/ask_booking_date.html', context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def choose_seat_view(request):
    movie = models.Movie.objects.get(id=request.session['movie_id'])
    seats = models.Seat.objects.get(id=request.session['seat_id'])
    dict = {
        'movie': movie,
        'seats': seats,
    }
    response = render(request, 'multiplex/choose_seat.html', context=dict)
    response.set_cookie('movie_id', request.session['movie_id'])
    response.set_cookie('seat_id', request.session['seat_id'])
    return response


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def proceed_to_pay_view(request):
    total = int(request.COOKIES['allNumberVals']) * 100
    totalSeat = int(request.COOKIES['allNumberVals'])
    return render(request, 'multiplex/payment.html', {'total': total, 'totalSeat': totalSeat})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def payment_success_view(request):
    movie = models.Movie.objects.get(id=request.COOKIES['movie_id'])
    seats = models.Seat.objects.get(id=request.COOKIES['seat_id'])
    allNameVals = request.COOKIES['allNameVals']
    allNumberVals = request.COOKIES['allNumberVals']
    allSeatsVals = request.COOKIES['allSeatsVals']
    total = int(request.COOKIES['allNumberVals']) * getattr(movie, 'price')

    # make seat unavailable for other
    seat = allSeatsVals.split(',')
    for x in seat:
        if x == 'A1':
            seats.A1 = False
        elif x == 'A2':
            seats.A2 = False
        elif x == 'A3':
            seats.A3 = False
        elif x == 'A4':
            seats.A4 = False
        elif x == 'A5':
            seats.A5 = False
        elif x == 'A6':
            seats.A6 = False
        elif x == 'A7':
            seats.A7 = False
        elif x == 'A8':
            seats.A8 = False
        elif x == 'A9':
            seats.A9 = False
        elif x == 'A10':
            seats.A10 = False
        elif x == 'A11':
            seats.A11 = False
        elif x == 'A12':
            seats.A12 = False
        elif x == 'B1':
            seats.B1 = False
        elif x == 'B2':
            seats.B2 = False
        elif x == 'B3':
            seats.B3 = False
        elif x == 'B4':
            seats.B4 = False
        elif x == 'B5':
            seats.B5 = False
        elif x == 'B6':
            seats.B6 = False
        elif x == 'B7':
            seats.B7 = False
        elif x == 'B8':
            seats.B8 = False
        elif x == 'B9':
            seats.B9 = False
        elif x == 'B10':
            seats.B10 = False
        elif x == 'B11':
            seats.B11 = False
        elif x == 'B12':
            seats.B12 = False
        elif x == 'C1':
            seats.C2 = False
        elif x == 'C3':
            seats.C3 = False
        elif x == 'C4':
            seats.C4 = False
        elif x == 'C5':
            seats.C6 = False
        elif x == 'C7':
            seats.C8 = False
        elif x == 'C9':
            seats.C9 = False
        elif x == 'C10':
            seats.C10 = False
        elif x == 'C11':
            seats.C11 = False
        elif x == 'C12':
            seats.C12 = False
        elif x == 'D1':
            seats.D1 = False
        elif x == 'D2':
            seats.D2 = False
        elif x == 'D3':
            seats.D3 = False
        elif x == 'D4':
            seats.D4 = False
        elif x == 'D5':
            seats.D5 = False
        elif x == 'D6':
            seats.D6 = False
        elif x == 'D7':
            seats.D7 = False
        elif x == 'D8':
            seats.D8 = False
        elif x == 'D9':
            seats.D9 = False
        elif x == 'D10':
            seats.D10 = False
        elif x == 'D11':
            seats.D11 = False
        elif x == 'D12':
            seats.D12 = False
        elif x == 'E1':
            seats.E1 = False
        elif x == 'E2':
            seats.E2 = False
        elif x == 'E3':
            seats.E3 = False
        elif x == 'E4':
            seats.E4 = False
        elif x == 'E5':
            seats.E5 = False
        elif x == 'E6':
            seats.E6 = False
        elif x == 'E7':
            seats.E7 = False
        elif x == 'E8':
            seats.E8 = False
        elif x == 'E9':
            seats.E9 = False
        elif x == 'E10':
            seats.E10 = False
        elif x == 'E11':
            seats.E11 = False
        elif x == 'E12':
            seats.E12 = False
        elif x == 'F1':
            seats.F1 = False
        elif x == 'F2':
            seats.F2 = False
        elif x == 'F3':
            seats.F3 = False
        elif x == 'F4':
            seats.F4 = False
        elif x == 'F5':
            seats.F5 = False
        elif x == 'F6':
            seats.F6 = False
        elif x == 'F7':
            seats.F7 = False
        elif x == 'F8':
            seats.F8 = False
        elif x == 'F9':
            seats.F9 = False
        elif x == 'F10':
            seats.F10 = False
        elif x == 'F11':
            seats.F11 = False
        elif x == 'F12':
            seats.F12 = False
        elif x == 'G1':
            seats.G1 = False
        elif x == 'G2':
            seats.G2 = False
        elif x == 'G3':
            seats.G3 = False
        elif x == 'G4':
            seats.G4 = False
        elif x == 'G5':
            seats.G5 = False
        elif x == 'G6':
            seats.G6 = False
        elif x == 'G7':
            seats.G7 = False
        elif x == 'G8':
            seats.G8 = False
        elif x == 'G9':
            seats.G9 = False
        elif x == 'G10':
            seats.G10 = False
        elif x == 'G11':
            seats.G11 = False
        elif x == 'G12':
            seats.G12 = False
        elif x == 'H1':
            seats.H1 = False
        elif x == 'H2':
            seats.H2 = False
        elif x == 'H3':
            seats.H3 = False
        elif x == 'H4':
            seats.H4 = False
        elif x == 'H5':
            seats.H5 = False
        elif x == 'H6':
            seats.H6 = False
        elif x == 'H7':
            seats.H7 = False
        elif x == 'H8':
            seats.H8 = False
        elif x == 'H9':
            seats.H9 = False
        elif x == 'H10':
            seats.H10 = False
        elif x == 'H11':
            seats.H11 = False
        elif x == 'H12':
            seats.H12 = False
        elif x == 'I1':
            seats.I1 = False
        elif x == 'I2':
            seats.I2 = False
        elif x == 'I3':
            seats.I3 = False
        elif x == 'I4':
            seats.I4 = False
        elif x == 'I5':
            seats.I5 = False
        elif x == 'I6':
            seats.I6 = False
        elif x == 'I7':
            seats.I7 = False
        elif x == 'I8':
            seats.I8 = False
        elif x == 'I9':
            seats.I9 = False
        elif x == 'I10':
            seats.I10 = False
        elif x == 'I11':
            seats.I11 = False
        elif x == 'I12':
            seats.I12 = False
        elif x == 'J1':
            seats.J1 = False
        elif x == 'J2':
            seats.J2 = False
        elif x == 'J3':
            seats.J3 = False
        elif x == 'J4':
            seats.J4 = False
        elif x == 'J5':
            seats.J5 = False
        elif x == 'J6':
            seats.J6 = False
        elif x == 'J7':
            seats.J7 = False
        elif x == 'J8':
            seats.J8 = False
        elif x == 'J9':
            seats.J9 = False
        elif x == 'J10':
            seats.J10 = False
        elif x == 'J11':
            seats.J11 = False
        elif x == 'J12':
            seats.J12 = False

    seats.save()
    # create booking object
    customer = models.Customer.objects.get(user_id=request.user.id)
    booking = models.Booking()
    booking.customer = customer
    booking.movie = movie
    booking.cost = total
    booking.totalSeat = int(request.COOKIES['allNumberVals'])
    booking.seatNumber = allSeatsVals
    booking.date = seats.date
    booking.watchers = allNameVals
    booking.save()

    return render(request, 'multiplex/movie_booked.html', {'customer': customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_feedback_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    feedback = forms.FeedbackForm()
    if request.method == 'POST':
        feedback = forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request, 'multiplex/feedback_sent_by_customer.html', {'customer': customer})
    return render(request, 'multiplex/customer_feedback.html', {'feedback': feedback, 'customer': customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_ticket_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    bookings = models.Booking.objects.filter(customer=customer).order_by('-id')
    dict = {
        'customer': customer,
        'bookings': bookings,
    }
    return render(request, 'multiplex/customer_ticket.html', context=dict)
