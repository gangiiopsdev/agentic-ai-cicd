from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
    def ping(host):
        try:
            completed_process = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": completed_process.stdout}
        except subprocess.CalledProcessError as e:
            raise ValueError(f"Ping failed: {e.stderr}")

app = FastAPI()
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):  # Validate the host input
        return CommandExecutor.ping(host)
    else:
        raise ValueError("Invalid host")