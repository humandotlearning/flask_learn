from app import app

@app.route('/')
@app.route('/index')
def index():
    user= {'username': 'miguel'}
    return '''
    <html>
        <head>
            <title> hello world </title>
        </head>
        <body>
            <h1> hello ''' + user['username'] + ''' </h1>
        </body>
    </html>
    '''