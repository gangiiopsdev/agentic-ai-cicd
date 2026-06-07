from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric() and len(host) <= 3:
        # Safe ping implementation using list arguments
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isnumeric() or len(host) > 3:
        return {"error": "Invalid input"}, 400
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}, 500