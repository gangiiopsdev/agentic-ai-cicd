from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input more strictly
        if not all(c.isalnum() or c in ['.', '-'] for c in host) or len(host) > 253:
            raise ValueError("Invalid host name")
        result = subprocess.run(['ping', f'"{host}"'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": str(e)}