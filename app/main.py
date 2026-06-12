from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if not v.startswith(('192.168.', '10.', '172.')):
            raise ValueError('Invalid host IP address')
        return v

    try:
        output = subprocess.check_output(['ping', '-c', '4', validate_host(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "error", "message": str(e)}