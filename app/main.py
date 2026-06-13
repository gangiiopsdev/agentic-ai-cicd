from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is safe
    if not host.strip().isalnum():
        return {"status": "error", "response": "Invalid input"}

    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return {"status": "completed", "response": result.stdout}