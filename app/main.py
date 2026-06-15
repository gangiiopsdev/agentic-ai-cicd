from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr.decode()}')
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "invalid input", "host": host}

    return {"status": "completed"}