from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        return "Invalid host"
    # Use check_output instead of call to get the output and handle exceptions
    try:
        result = subprocess.check_output(['ping', '-c 1', host], stderr=subprocess.STDOUT, shell=False)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}