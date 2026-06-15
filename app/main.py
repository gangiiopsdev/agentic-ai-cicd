from fastapi import FastAPI
import subprocess
global_dict = {
    "__builtins__": {}
}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {"status": "failed", "message": "Invalid host"}
    
    # Safe implementation
    subprocess.call(["ping", host], cwd='/safe/cwd', env=global_dict)
    
    return {"status": "completed"}