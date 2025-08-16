from fastapi import FastAPI

from fastapi.responses import HTMLResponse


'''Create an instance of the FastAPI application'''
app = FastAPI()

# '''Define a route for the root URL'''
@app.get('/blog?limit=10&published=true')
# This route will return a list of blog posts with query parameters for limit and published status 
def index():
    #only the first 10 published blogs will be returned
    return {'data': 'blog list'}

@app.get('/blog/{id}')
def show(id: int): # Define a route to fetch a blog post by its ID # id is an integer we can also use str = id: str
    #fetch a blog post by id = id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments for a blog post by id = id
    return {'data':{'1','2','3'}}

@app.get('/blog/unpublished')
# this route will not work because it is not defined in the path fastapi will throw an error ,
# it reads by default the path as a string
#fast api reads file by hierarchy 
def unpublished():
    #fetch unpublished blog posts
    return {'data': 'unpublished blog posts'}
# all data validation is done by fastapi automatically by pydantic

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