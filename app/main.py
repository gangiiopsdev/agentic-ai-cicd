from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        if result.returncode == 0:
            return 'ping successful'
        else:
            return f'ping failed: {result.stderr}'
    except Exception as e:
        return f'error: {str(e)}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {"status": result}