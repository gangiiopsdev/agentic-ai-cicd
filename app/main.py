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
    # Safe implementation
    subprocess.call(["ping", host], cwd='/safe/cwd', env=global_dict)
    
    return {"status": "completed"}