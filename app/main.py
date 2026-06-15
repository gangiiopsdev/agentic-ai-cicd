from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_ping_command(host):
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(create_ping_command(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}