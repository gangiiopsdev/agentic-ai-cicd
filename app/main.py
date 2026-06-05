from fastapi import FastAPI
import subprocess
import shlex
class SanitizeInput:
    @staticmethod
def sanitize(input_string):
        return ''.join(e for e in input_string if e.isalnum() or e in [".", "-"])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = SanitizeInput.sanitize(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}