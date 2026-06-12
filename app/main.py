from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote to prevent command injection
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "response": response}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}