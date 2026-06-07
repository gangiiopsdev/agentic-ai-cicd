from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.list2cmdline([host])
        try:
            output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode('utf-8')}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError('Invalid hostname')
    return SafeSubprocess.ping(host)