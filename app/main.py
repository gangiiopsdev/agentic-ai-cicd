from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.' or e == '-').strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = subprocess.run(['ping', sanitize_input(host)], capture_output=True, text=True)
    return {"status": "completed", "output": sanitized_host.stdout}