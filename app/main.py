from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):    
    escaped_host = escape_user_input(host)
    subprocess.call(f"ping {escaped_host}", shell=False)
    return {"status": "completed"}