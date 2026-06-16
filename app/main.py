from fastapi import FastAPI
import subprocess
given_host = '8.8.8.8' # Replace with a fixed or validated host for demonstration purposes
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.check_output(['ping', given_host], stderr=subprocess.STDOUT)
        return {"status": "completed", "host": given_host}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}