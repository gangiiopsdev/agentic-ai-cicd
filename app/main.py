from fastapi import FastAPI, HTTPException
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        if not host:
            raise ValueError("Host cannot be empty")
        # Sanitize the input before using it in subprocess
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['-', '.'])
        command = shlex.split(f'ping {sanitized_host}')
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}