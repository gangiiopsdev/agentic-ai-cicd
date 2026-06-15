from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host is a valid IP address to mitigate risks
    import re
    if not re.match(r'^[0-9]{1,3}([.][0-9]{1,3}){3}$', host):
        return {"status": "error", "message": "Invalid IP address"}
    response = execute_ping(host)
    return {"status": "completed", "response": response}