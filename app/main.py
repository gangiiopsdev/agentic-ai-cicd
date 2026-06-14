from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return str(e), None

@app.get("/ping")
def ping(host: str):
    output, error = execute_ping(host)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}