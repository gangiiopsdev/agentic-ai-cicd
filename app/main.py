from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with check=True and text=True
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "output": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}