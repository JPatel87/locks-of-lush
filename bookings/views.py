"""Imports from django, booking model and booking forms."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingFormAdmin, BookingForm


def bookings(request):
    """
    Function to view bookings page.

    If user is an admin, they see all
    user bookings else all other users will
    only see their bookings.Both are
    ordered in date order (earliest first).
    """

    if request.user.is_superuser:
        booking = Booking.objects.all().order_by('date')
        context = {
            'bookings': booking
        }
    else:
        user_filter = Booking.objects.filter(user__in=[request.user])
        booking = user_filter.order_by('date')
        context = {
            'bookings': booking
        }
    return render(request, 'bookings/bookings.html', context)


def add_bookings(request):
    """
    Function to view add bookings page.

    The get request returns the add bookings form.
    Different forms for admin and non-admin users.
    The post request checks the form is valid,
    displays validity message, returns bookings page
    if valid.
    """
    if request.method == 'POST':
        if request.user.is_superuser:
            form = BookingFormAdmin(request.POST)
            context = {
                'form': form
            }
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Request successful',
                    extra_tags='successful_request'
                )
                return redirect('bookings')
            else:
                messages.error(
                    request,
                    'Request unsuccessful - address errors',
                    extra_tags='unsuccessful_request'
                    )
                return render(request, 'bookings/add_bookings.html', context)
        else:
            form = BookingForm(request.POST)
            context = {
                'form': form
            }
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(
                    request,
                    'Request successful',
                    extra_tags='successful_request'
                )
                return redirect('bookings')
            else:
                messages.error(
                    request,
                    'Request unsuccessful - address errors',
                    extra_tags='unsuccessful_request'
                    )
                return render(request, 'bookings/add_bookings.html', context)
    else:
        if request.user.is_superuser:
            form = BookingFormAdmin
            context = {
                'form': form
            }
        else:
            form = BookingForm
    context = {
        'form': form
    }
    return render(request, 'bookings/add_bookings.html', context)


def edit_bookings(request, booking_id):
    """
    Function to view edit bookings page.

    The get request returns the edit bookings page.
    Different forms for admin and non-admin users.
    The post request checks the form is valid,
    displays validity message, returns bookings page if valid.
    """

    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        if request.user.is_superuser:
            form = BookingFormAdmin(request.POST, instance=booking)
            context = {
                'form': form
            }
        else:
            form = BookingForm(request.POST, instance=booking)
            context = {
                'form': form
            }

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Request successful',
                extra_tags='successful_request'
            )
            return redirect('bookings')
        else:
            messages.error(
                request,
                'Request unsuccessful - address errors',
                extra_tags='unsuccessful_request'
            )
            return render(request, 'bookings/edit_bookings.html', context)

    if request.user.is_superuser:
        form = BookingFormAdmin(instance=booking)
        context = {
            'form': form
        }
        return render(request, 'bookings/edit_bookings.html', context)
    else:
        form = BookingForm(instance=booking)
        context = {
            'form': form
        }
        return render(request, 'bookings/edit_bookings.html', context)


def delete_bookings(request, booking_id):
    """
    Function to view delete bookings page.

    The get request returns the delete bookings page.
    The post request deletes the booking,
    displays the success message, returns booking page.
    """

    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        messages.success(
            request,
            'Request successful',
            extra_tags='successful_request'
        )
        return redirect('bookings')
    context = {
        'bookings': booking
    }
    return render(request, 'bookings/delete_bookings.html', context)
