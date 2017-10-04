from flask import Flask, request, redirect, render_template


app = Flask(__name__)

app.config['DEBUG'] = True #displays runtime  errors

signup_form = """
    <style>
        .error {{color: red;}}
    </style>
    <h1>Sign-Up</h1>
    <form method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
            <p class="error">{username_error}</p>
        <label>Password
            <input name="password" type="password" value='{password}' />
        </label>
        <p class="error">{password_error}</p>
        <label>Verify Password
            <input name="pwverify" type="password" value='{pwverify}' />
        </label>
        <p class="error">{pwverify_error}</p>
        <label>Email (Optional)
            <input name="email" type="text" value='{email}' />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Validate" />
    </form>
    """

@app.route('/')
def display_signup_form():
    return signup_form.format(username='', username_error='',
       password='', password_error='', pwverify='', pwverify_error='', email='', email_error='')


@app.route('/', methods=['POST'])
def validate_signup():
    
    username = request.form['username']
    password = request.form['password']
    pwverify = request.form['pwverify']
    email = request.form['email']

    username_error=''
    password_error=''
    pwverify_error=''
    email_error=''
    
    #username validation
    if len(username) < 3:
        if username =='':
            username_error='Please enter a username.'
        else:
            username_error='Username must have more than 3 characters.'
    for i in username:
        if i == ' ':
            username_error='Spaces are not allowed in username'
    if len(username) > 20:
            username_error='User name must be less than 20 characters.'  

    #password validation
    if len(password) < 3:
        if password =='':
            password_error='Please enter a password.'
        else:
            password_error='Password must have more than 3 characters.'
    for i in password:
        if i == ' ':
            password_error='Spaces are not allowed in password.'
    if len(password) > 20:
            password_error='Password  must be less than 20 characters.'

    #pwverify validation

    if pwverify != password:
        pwverify_error = "Passwords don't match."

    #email validation


    
        

    #if not is_integer(minutes):
       # minutes_error='Not a valid integer'
       # minutes = ''
    #else:
            #minutes = int(minutes)
           # if minutes > 59 or minutes < 0:
                #minutes_error = 'Minute value out of range (0-59)'
               # minutes = ''

    if not username_error and not password_error and not pwverify_error and not email_error:
        return "Success!"
    else:
        return signup_form.format(username_error=username_error, password_error=password_error, username=username,
       password=password, pwverify=pwverify, pwverify_error=pwverify_error, email=email, email_error=email_error) 
         

    

app.run()