from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + [sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "status": "failed"}