from fastapi import FastAPI
import subprocess
get_whoami = subprocess.getoutput('whoami')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}