from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}

    # Escape special characters in the host parameter to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    args = ["ping", safe_host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}