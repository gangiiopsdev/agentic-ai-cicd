from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        # Validate and sanitize input to prevent command injection
        if not host.strip() or '&&' in host or ';' in host or '|' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingCommand.run(host)