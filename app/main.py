from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    cmd = ' '.join(shlex.quote(a) for a in args)
    subprocess.run(cmd, shell=False, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}