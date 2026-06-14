from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        result = subprocess.run(['ping'], check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }