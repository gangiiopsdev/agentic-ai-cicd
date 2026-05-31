from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if host.isalnum():
        command = ["ping", host]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}