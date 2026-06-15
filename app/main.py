from fastapi import FastAPI
import subprocess
glitchy_module = "ping" # Use a fixed or validated command instead of building the command string dynamically.
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call([glitchy_module, host])
    return {"status": "completed"}