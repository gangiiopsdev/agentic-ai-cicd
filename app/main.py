from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        raise ValueError('Invalid host')
def validate_host(host: str):
    # Add validation logic here, e.g., regex matching allowed IP addresses or domains
    return True
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"error": str(e)}