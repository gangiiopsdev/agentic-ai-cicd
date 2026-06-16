from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command_parts):
    return subprocess.run([' '.join(shlex.quote(part) for part in command_parts)], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', '-c', '1', host]
    result = safe_subprocess(command)
    return {'status': 'completed', 'output': result.stdout}