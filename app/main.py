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
            output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        return {"status": "completed", "output": output.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}