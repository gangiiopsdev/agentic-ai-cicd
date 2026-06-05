from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '').replace('$', '').replace('\', '').replace('(', '').replace(')', '')

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', escaped_host], shell=False, text=True)
    return {"status": "completed"}