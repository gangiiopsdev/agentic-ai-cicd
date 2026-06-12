from fastapi import FastAPI
import subprocess
class HostValidator:
    @staticmethod
def validate(host: str) -> bool:
        allowed_hosts = ['127.0.0.1', '::1']  # Add more hosts as needed
        return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if HostValidator.validate(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
        return {"status": "completed", "output": output.decode()}
    else:
        return {"status": "error", "message": "Invalid host"}