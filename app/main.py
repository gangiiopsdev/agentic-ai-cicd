from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['google.com', 'example.com']
    if host in valid_hosts:
        try:
            result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
            return {
                "status": "completed",
                "result": "Ping successful",
                "output": result.decode()
            }
        except subprocess.CalledProcessError as e:
            return {
                "status": "failed",
                "error": e.output.decode()
            }
    else:
        return {
            "status": "failed",
            "error": "Invalid host"
        }

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)