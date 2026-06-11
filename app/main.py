from fastapi import FastAPI
import subprocess
def escape_command(input):
    return input.replace(";", "\x3b").replace("&", "\x26")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_command(host)
    subprocess.call(f'ping {escaped_host}', shell=False)
    return {"status": "completed"}