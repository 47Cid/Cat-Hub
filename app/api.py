from flask import render_template, url_for, flash, redirect, request, render_template_string
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.forms import RegistrationForm, LoginForm, CommentForm, SettingsForm
from app.models import User, Comment, AppSettings
from app import login_manager
from app.config_headers import add_security_headers
import requests

@app.route("/products")
def api():
    # Read the HOST header and make a request to the API server using the host 
    host = request.headers.get('Host')
    
    # Check if the host is valid
    if 'localhost:3000' not in host:
        return {"error": "Invalid host."}
    
    response = requests.get(f"http://{host}/api/v1/products")
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()
    else:
        return {"error": "Unable to fetch products."}
