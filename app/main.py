from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], check=True, capture_output=True, text=True)
        return {"status": "completed", "response": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "response": str(e)}