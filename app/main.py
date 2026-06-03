from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def run_ping(host):
        try:
            # Validate and sanitize the host input
            if not all(c.isalnum() or c in '._-' for c in host):
                raise ValueError('Invalid hostname')
            safe_host = shlex.quote(host)
            output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeCommand.run_ping(host)
    return {"status": "completed", "result": result}