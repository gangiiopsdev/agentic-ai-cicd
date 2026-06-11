from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def safe_ping(host):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Add validation for the host parameter
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"status": "error", "message": "Invalid input"}
    try:
        response = Ping.safe_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Improved validation to prevent command injection
@app.get("/ping_secure")
def ping_secure(host: str):  # Add validation for the host parameter
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"status": "error", "message": "Invalid input"}
    try:
        response = Ping.safe_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}