
def get_user_role(request):
    user = request.user

    try:
        if user.userdetails:
            role = user.userdetails.user_type
        
    except:
        try:
            if user.multivenders:
                role = user.multivenders.user_type
        except:
            role = "admin"
    finally:
        return role