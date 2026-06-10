from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}