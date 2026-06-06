from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    return host in allowed_hosts