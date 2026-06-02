from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        raise cimport(f'Ping failed with return code {result.returncode}: {result.stderr}')

    return {"status": "completed", "stdout": result.stdout}