from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "result": "Invalid host"}
    result = run_ping(host)
    return {"status": "completed", "result": result}