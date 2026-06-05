from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Stronger regex to validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}