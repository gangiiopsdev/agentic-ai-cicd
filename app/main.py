from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape host
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}