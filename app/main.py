from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', '-c', '1', '--', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    response = safe_ping(host)
    return {"status": "completed", "response": response}