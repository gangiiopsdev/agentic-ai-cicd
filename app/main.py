from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allowed IP ranges or domains
    return True

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "result": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr.decode()}
    return {"status": "not_validated"}