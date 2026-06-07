from fastapi import FastAPI
import subprocess
global_host = "127.0.0.1"  # Replace with a fixed or validated host value

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if host != global_host:
        raise HTTPException(status_code=403, detail="Unauthorized access")
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}