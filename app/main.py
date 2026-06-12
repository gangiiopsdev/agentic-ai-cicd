from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate host input to ensure it's a valid domain name or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,
global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = global_safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}
    return {"status": "completed", "output": result}