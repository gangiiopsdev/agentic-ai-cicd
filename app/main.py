from fastapi import FastAPI
import subprocess
def safe_ping(host):
    valid_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in valid_hosts:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)