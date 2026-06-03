from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add any necessary input sanitization here
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}