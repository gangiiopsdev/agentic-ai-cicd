from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(host)
    result = execute_ping(sanitized_host)
    return {"status": "completed", "result": result}