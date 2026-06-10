from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using shell=False and passing arguments as a list instead of using f-strings in shell=True
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):  
    safe_ping(host)
    return {"status": "completed"}