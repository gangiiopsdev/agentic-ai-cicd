from fastapi import FastAPI
import subprocess
from os.path import abspath

app = FastAPI()

def safe_ping(host):
    try:
        # Validate host input to prevent shell injection attacks
        if not host.isalnum():
            raise ValueError("Invalid host")
        result = subprocess.run([abspath('ping'), host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))
    except ValueError as ve:
        return str(ve)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)