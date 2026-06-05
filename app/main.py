from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    command = ['ping', '--'] + [host]  # Use -- to prevent argument injection
    subprocess.run(command, check=True)
    return {"status": "completed"}