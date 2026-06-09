from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not all(c in string.ascii_letters + string.digits for c in host):
        raise ValueError('Invalid input')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}