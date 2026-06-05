from fastapi import FastAPI
import subprocess
def escape_host(host):
    # Escape special characters that could be used for command injection
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run to avoid shell=True and improve security
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}