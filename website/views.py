from flask import Blueprint #imported blueprint

views =  Blueprint('views', __name__) # created view, this view name can be anything. 
                                      # Kept name same as file name for better understanding

@views.route('/') # here views is the name of the blueprint which we gave above. 
                 # inside (), we will give the url name
def home(): # home is a function, this will run whenever / route will get called
    return "<h1>Meeting with old friend</h1>"