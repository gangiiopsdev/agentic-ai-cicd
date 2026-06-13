from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement input sanitization here
    return ''.join(e for e in input_str if e.isalnum())

@app.get("/ping")
def ping(host: str):    host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}