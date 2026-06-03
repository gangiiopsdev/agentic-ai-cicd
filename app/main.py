from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    output = safe_ping(shlex.quote(host))  # Quote the input to prevent command injection
    return {"status": "completed", "output": output}