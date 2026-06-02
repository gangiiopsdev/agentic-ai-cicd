from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize host input to prevent command injection
        safe_host = re.sub(r'[^a-zA-Z0-9-.!]', '', host)
        args = ['ping', '--', safe_host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)}