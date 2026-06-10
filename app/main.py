from fastapi import FastAPI
import subprocess
import shlex
class InputSanitizer:
    @staticmethod
def sanitize_input(input_str):
        return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = InputSanitizer.sanitize_input(host)
    # Secure implementation using subprocess.Popen instead of shlex.split and subprocess.run
cmd = ['ping', sanitized_host]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
if process.returncode == 0:
    return {"status": "completed", "output": stdout}
else:
    return {"status": "failed", "error": stderr}