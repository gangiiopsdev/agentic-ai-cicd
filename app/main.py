from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.run(['ping', f'"{sanitized_host}"'], capture_output=True, text=True)
    return {"status": "completed", "output": sanitized_host.stdout}