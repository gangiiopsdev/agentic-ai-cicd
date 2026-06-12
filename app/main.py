from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
        if host not in allowed_hosts:
            raise ValueError(f'Host {host} is not allowed')
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the input
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        status = SafePing.safe_ping(host)
        return {"status": "completed", "output": status}
    except Exception as e:
        return {"error": str(e)}