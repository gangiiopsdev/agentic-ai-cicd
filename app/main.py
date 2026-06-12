from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex to safely quote the host input
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}