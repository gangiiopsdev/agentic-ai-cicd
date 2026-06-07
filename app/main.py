from fastapi import FastAPI
import re
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate the host input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}