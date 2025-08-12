from fastapi import FastAPI

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