from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    allowed_hosts = ['example.com', 'test.com']  # Example allowed hosts
    if host not in allowed_hosts:
        return {"error": "Host not allowed"}, 403
    args = shlex.split(f"ping {host}")
    subprocess.run(args)
    return {"status": "completed"}