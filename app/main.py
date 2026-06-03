from fastapi import FastAPI
import subprocess
def validate_host(host):
    return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=False)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"status": "failed", "error": str(e)}