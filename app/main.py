from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
    def ping(host: str):
        if not host.strip():
            return "Invalid input"
        # Sanitize the input to prevent command injection
        safe_host = subprocess.quote(host)
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePinger.ping(host)