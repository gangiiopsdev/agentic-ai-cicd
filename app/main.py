from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input to avoid command injection
        safe_host = shlex.quote(host)
        # Use subprocess.run instead of subprocess.call for better security and error handling
        result = subprocess.run(f"ping {safe_host}", shell=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}