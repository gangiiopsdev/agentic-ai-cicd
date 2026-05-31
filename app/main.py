from fastapi import FastAPI
import subprocess
callable = subprocess.run

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = callable(['ping', host], shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}