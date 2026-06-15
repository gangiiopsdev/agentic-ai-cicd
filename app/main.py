from fastapi import FastAPI
import subprocess
class SanitizedPing:
    @staticmethod
def execute(host: str):
        if not host or len(host) > 255:
            raise ValueError('Invalid host input')
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-.')
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SanitizedPing.execute(host)