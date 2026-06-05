from fastapi import FastAPI
import re

def sanitize_input(input_str):
    # Advanced sanitization: remove non-alphanumeric characters and escape shell metacharacters
    return re.sub(r'[^a-zA-Z0-9]', '', input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):,
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
    return {"status": "completed", "output": result.stdout}