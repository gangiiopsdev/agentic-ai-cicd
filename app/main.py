from fastapi import FastAPI
import subprocess
import shlex
class SanitizedInput:
    @staticmethod
    def sanitize_input(value):
        return ''.join(e for e in value if e.isalnum() or e in ['-', '.', '_', '/', ':'])

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
async def ping(host: str):
    sanitized_host = SanitizedInput.sanitize_input(host)
    try:
        output = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, timeout=5)
        return {'status': 'completed' if output.returncode == 0 else 'error', 'output': output.stdout}
    except subprocess.TimeoutExpired as e:
        return {'status': 'timeout', 'output': str(e)}