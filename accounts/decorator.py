from django.shortcuts import redirect



# Decorator for logout_required
def logout_required(view_func):
    '''
    Docstring for logout_required
    if user is loged in restrict them to access login, register page.
    
    :param view_func: Description
    '''
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper