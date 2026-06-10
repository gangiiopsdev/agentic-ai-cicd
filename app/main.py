from fastapi import FastAPI
import subprocess
global_result = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.Popen with shell=False and passing args as a list
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        global_result[host] = result.stdout
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}