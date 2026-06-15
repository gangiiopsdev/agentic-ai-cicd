from fastapi import FastAPI
import subprocess
class SanitizeInput:
    @staticmethod
def sanitize_host(host):
        return ''.join(e for e in host if e.isalnum() or e in [':', '.', '-'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = SanitizeInput.sanitize_host(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}