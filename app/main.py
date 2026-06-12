from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = '0123456789'
    if all(c in allowed_chars for c in input_str) and len(input_str) <= 3:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {"status": "failed", "error": "Invalid input for ping"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}