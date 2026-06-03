from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    return 'ping {host}'.format(host=host)

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), shell=True, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}