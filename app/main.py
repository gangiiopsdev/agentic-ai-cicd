from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Add your sanitization logic here
    return user_input.strip()

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}