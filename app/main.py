from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.run(['ping', escaped_host], check=True)  # Use subprocess.run for safer execution
    return {"status": "completed"}