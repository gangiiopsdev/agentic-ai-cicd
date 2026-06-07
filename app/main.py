from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation with shell=False and argument checking
    if not host:
        return False
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        print(result.stdout.decode())
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "completed", "result": "failure"}