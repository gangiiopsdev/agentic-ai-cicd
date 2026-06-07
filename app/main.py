from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using check_output instead of call for better error handling and security
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/ping")
def ping(host: str):
    # Using a safe function to avoid shell=True
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}