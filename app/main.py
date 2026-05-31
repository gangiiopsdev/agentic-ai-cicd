from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess_call(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    safe_host = host  # Assume the input is already sanitized or limited to known good values
    command = ['ping', safe_host]
    result = safe_subprocess_call(command)
    return {'status': 'completed', 'output': result}