from fastapi import FastAPI
import subprocess
gl = get_logger(__name__)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        gl.error(f'Ping failed for {host}: {e.stderr.decode()}')
    return {"status": "completed"}