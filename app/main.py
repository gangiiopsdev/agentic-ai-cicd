from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', '--', host]  # Adding '--' to prevent argument injection
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout
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