from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str) -> str:
    return shlex.quote(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        args = shlex.split(f'ping -c 1 {escaped_host}')  # Limit the number of pings to reduce potential DoS
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}