from functools import wraps
from flask import request,redirect,url_for,flash
import re


def requiremobile(func):
    """Decorator to ensure that only users on mobile can access the app parts of the website."""
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        ua =  request.headers.get('User-Agent')
        match = re.search("Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini",ua)
        if match:
            return func(*args,**kwargs) #Do nothing
        else:
            flash("Note: you have tried to access a page that requires you to be on mobile. Please try again on your phone.")
            return redirect(url_for("home_bp.home"), code=302)
    
    return wrapper

