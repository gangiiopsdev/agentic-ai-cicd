from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run without shell=True for safer execution
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safely execute ping command
    output = safe_ping(host)
    return {"status": "completed", "output": output}