from fastapi import FastAPI


app = FastAPI()

@app.get('/ping/')
def check_homework_03():
    return {"message": "pong"}