from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_user_input(host)
    # Use a list to pass arguments safely instead of shell=True
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}