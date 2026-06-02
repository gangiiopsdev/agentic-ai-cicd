from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate user input to prevent command injection
    if not host.isalnum() or ' ' in host:
        return {"status": "error", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', '--icmp-type=echo', host], check=True, text=True, capture_output=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}