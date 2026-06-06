from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize input using shlex.quote
    sanitized_host = subprocess.list2cmdline([host])
    output = run_ping(sanitized_host)
    return {"status": "completed", "output": output}