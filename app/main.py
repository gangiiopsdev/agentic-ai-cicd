from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}

    # Safe implementation using subprocess.run for better control and security
    args = ["ping", host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}