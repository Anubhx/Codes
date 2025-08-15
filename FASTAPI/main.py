from fastapi import FastAPI

from fastapi.responses import HTMLResponse


'''Create an instance of the FastAPI application'''
app = FastAPI()

# '''Define a route for the root URL'''
@app.get('/') 
def index():
    return {'data':{'name':'John Doe', 'age': 30, 'city': 'New York'}}
# '''Define a route for the about page'''
@app.get('/about')
def about():
    return {'data':{'about page'}}
# '''Define a route for the HTML response'''
# Import HTMLResponse to return HTML content
#from fastapi.responses import HTMLResponse
@app.get('/html', response_class=HTMLResponse)
def html():
    return """
    <html>
        <head>
            <title>About Page</title>
        </head>
        <body>
            <h1>About Us</h1>
            <p>This is a basic web page served by FastAPI.</p>
            <button onclick="alert('Hello, World!')">Click Me!</button>
        </body>
    </html>
    """