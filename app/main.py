from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    result = execute_ping(safe_host)
    return {'status': 'completed', 'result': result}