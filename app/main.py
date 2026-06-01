from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate the host parameter to prevent command injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}