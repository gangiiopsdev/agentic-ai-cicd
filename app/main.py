from fastapi import FastAPI
import subprocess
given_host = 'example.com'  # Replace with proper validation logic for host parameter
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', given_host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {"status": "completed"}