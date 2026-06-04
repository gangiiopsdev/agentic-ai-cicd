from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    # Use subprocess.run safely by avoiding shell=True and using a list for the command
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}