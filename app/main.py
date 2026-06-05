from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}