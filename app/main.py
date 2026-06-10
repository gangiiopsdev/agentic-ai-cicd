from fastapi import FastAPI, Query
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate the host input to prevent injection attacks
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '1', host]  # Limit the number of pings to mitigate DDoS risk
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str = Query(..., min_length=1, max_length=255)):
    try:
        output = SafePing.safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}