from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        response = subprocess.run(["ping", "-c", "1", "/bin/sh"], capture_output=True, text=True, check=True)
        return {'stdout': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}