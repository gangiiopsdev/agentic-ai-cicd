from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    safe_host = escape_user_input(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}