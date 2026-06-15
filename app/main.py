from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Regular expression to validate the host input
    if not re.match(r'^[a-zA-Z0-9.-_!@#$%^&*()+=\[\]{}|;:,.<>?/`]*$', host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}