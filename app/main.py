from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = secure_ping(host)
    if isinstance(output, str) and 'command not found' in output:
        return {"status": "failed", "error": "Invalid command"}
    else:
        return {"status": "completed", "output": output}