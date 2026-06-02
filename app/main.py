from fastapi import FastAPI
import re
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize host input to prevent command injection
        safe_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
        args = ['ping', '-c', '1', safe_host]
        try:
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': ''}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)}