from django.shortcuts import redirect

def admin_only(view_func) :
    def wrapper_func(request, *args, **kwargs) :
        group = None
        if request.user.groups.exists() :
            group = request.user.groups.all()[0].name
        if group == 'admins' :
            return view_func(request, *args, **kwargs)
        if group == 'students' :
            return redirect('/studentDashboard')

    return wrapper_func