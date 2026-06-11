from fastapi import FastAPI
import subprocess
def escape_user_input(input_string):
    return input_string.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = escape_user_input(host)
    subprocess.call(f'ping {host}')
    return {"status": "completed"}