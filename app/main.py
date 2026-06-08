from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            cmd = ['ping', host]
            output = subprocess.run(cmd, check=True, stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    # Sanitize input to avoid command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    result = SafePing.ping(host)
    return result

# Preventive controls:
# 1. Use a whitelist of allowed hosts instead of a blacklist.
# 2. Validate and sanitize inputs more strictly, considering all possible characters.
# 3. Consider using parameterized queries or libraries designed to avoid command injection.