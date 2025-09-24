from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    # return 'Hello, World!'
    return {'data': {'name':'Raj Aryan'}}

@app.get("/about")
def about():
    return {'about':'I am a AI-ML Intern at OMNIe Solution (I) Pvt Ltd'}