from fastapi import FastAPI


app = FastAPI()

@app.get('/ping/')
def test_homework_03():
    return {"message": "pong"}