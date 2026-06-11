from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(input_string):
    return input_string.replace(';', '').replace('&', '').replace('&&', '').replace('|', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}