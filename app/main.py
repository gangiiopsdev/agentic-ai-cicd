from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host: str):
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = _ping(host)
    return {"status": result}