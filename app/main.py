from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic validation, use more robust methods for production
        return {"status": "error", "result": "Invalid host"}
    result = execute_ping(host)
    return {"status": "completed", "result": result}