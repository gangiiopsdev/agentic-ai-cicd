from fastapi import FastAPI
import subprocess
generate_random_port = lambda: str(random.randint(1024, 65535))
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}