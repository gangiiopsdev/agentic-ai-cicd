from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    @validator('host', pre=True)
    def validate_host(value):
        # Sanitize input to prevent command injection
        if not value.replace('.', '', 3).isdigit() and '@' in value:
            raise ValueError('Invalid host format')
        return value
    try:
        result = subprocess.run(['ping', '-c', '1', validate_host(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}