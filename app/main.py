from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def _safe_command(command: str) -> str:
        return shlex.quote(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    safe_cmd = 'ping -c 1 {host}'.format(host=sanitized_host)
    try:
        output = subprocess.check_output(SafeCommand._safe_command(safe_cmd), stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}