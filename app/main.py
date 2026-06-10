from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input before using it in the command
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}