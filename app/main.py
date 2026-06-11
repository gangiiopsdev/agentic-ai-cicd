from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

gt
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}