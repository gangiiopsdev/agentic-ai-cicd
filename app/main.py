from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    output = subprocess.getoutput(f'ping -c 1 {host}')
    return output

get_input = safe_ping

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        output = get_input(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}