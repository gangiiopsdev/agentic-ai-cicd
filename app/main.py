from fastapi import FastAPI
import subprocess
class SanitizedInput:
    def __init__(self, max_length=None):
        self.max_length = max_length

    def sanitize(self, input_string):
        if self.max_length is not None and len(input_string) > self.max_length:
            raise ValueError("Input too long")
        return ''.join(e for e in input_string if e.isalnum() or e.isspace())

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    sanitized_host = SanitizedInput(max_length=50).sanitize(host)
    result = subprocess.run(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}