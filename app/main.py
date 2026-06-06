from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip() == '':
        return {"status": "failed", "message": "Host is empty"}
    command = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)