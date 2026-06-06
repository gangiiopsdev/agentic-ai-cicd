from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' not in host:
        return False
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": "Ping successful."}
    else:
        return {"status": "failed", "message": "Ping failed or unsafe host specified."}