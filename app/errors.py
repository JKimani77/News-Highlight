from flask import render_template
from app import app

@app.errorhandler(404)
def errorfour_oh_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error.html'),404