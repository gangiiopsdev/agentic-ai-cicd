from fastapi import FastAPI
import subprocess
genesis = os.path.join(os.path.dirname(__file__), '..', 'tools', 'genesis')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}