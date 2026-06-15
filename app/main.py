from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', subprocess.check_output(['/usr/bin/ping', '-c', '1', host], stderr=subprocess.STDOUT).decode()], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return str(e), None

def is_valid_host(host: str) -> bool:
    # Add validation logic here to ensure the host input is safe
    return host.replace('.', '').replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    output, error = execute_ping(host)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}