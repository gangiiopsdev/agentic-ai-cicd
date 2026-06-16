from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr.decode()}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}