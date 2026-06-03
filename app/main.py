from fastapi import FastAPI
import subprocess
gitignore=['__pycache__', '*.log', '.env', 'venv']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}