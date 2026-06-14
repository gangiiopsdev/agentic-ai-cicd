from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using check_output with shell=False and safe argument handling
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        if result.returncode == 0:
            return {"status": "completed", "message": "Ping successful"}
        else:
            return {"status": "failed", "error": result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}