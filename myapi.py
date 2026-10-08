from fastapi import FastAPI

app = FastAPI()


#http request - get, post, put, patch, delete

#end point (url)
# www.sample.com/
# www.sample.com/login



@app.get("/")
def root():
    return {"message": "Hello World"}