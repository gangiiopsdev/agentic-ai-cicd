from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization, real-world use case should be more robust
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.call(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}