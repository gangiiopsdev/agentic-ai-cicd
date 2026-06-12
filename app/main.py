from fastapi import FastAPI
import subprocess
global_args = {"ping": "-c 4", "echo": "-n", "nslookup": ""}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with argument sanitization
    if host not in ["8.8.8.8", "127.0.0.1"]:
        raise ValueError("Invalid host")
    command = ['ping', '-c 4'] + [host]
    result = subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}