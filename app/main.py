from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_', ':', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] for c in host):
            return "Invalid hostname"
        try:
            result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)
global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = global_safe_ping(host)
    return {"status": "completed", "output": output}