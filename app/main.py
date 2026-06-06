from fastapi import FastAPI
import subprocess
global host = 'example.com'
app = FastAPI()
@app.get("/ping")
def ping():
    subprocess.call(['ping', host])
    return {"status": "completed"}