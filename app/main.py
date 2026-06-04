from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output.decode())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not (host.replace('.', '').isnumeric() and '@' not in host):
        return {"status": "error", "message": "Invalid input"}
    result = safe_ping(host)
    return {"status": "completed", "result": result}