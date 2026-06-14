from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": process.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}