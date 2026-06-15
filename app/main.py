from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run with properly formatted arguments
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid host"}
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    return PingService.ping(sanitized_host)