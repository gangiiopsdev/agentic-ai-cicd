from fastapi import FastAPI
import subprocess

def run_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class HostValidator:
    @staticmethod
def validate_host(host: str) -> bool:
        if not host.isalnum() and not '.' in host:
            return False
        return True

app = FastAPI()
@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if HostValidator.validate_host(host):
        output = run_ping(host)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host parameter"}