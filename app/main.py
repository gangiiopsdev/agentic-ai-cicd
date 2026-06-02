from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        command = ['ping', '-c', '1']
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError('Invalid input')
        command.append(quote_plus(host))
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}