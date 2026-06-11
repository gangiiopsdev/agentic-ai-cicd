from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
            return "Invalid hostname"
        try:
            result = subprocess.run(['ping', '-c 1', '--', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = global_safe_ping(host)
    return {"status": "completed", "output": output}