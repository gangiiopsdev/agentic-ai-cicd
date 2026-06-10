from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure the host parameter only contains valid characters
        if all(c.isalnum() or c in ('.', '-', '_') for c in host):
            try:
                result = subprocess.run(['ping', '-c', '1', '--', host], capture_output=True, text=True, check=True)
                return result.stdout
            except subprocess.CalledProcessError as e:
                return str(e)
        else:
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    response = SafePing.ping(host)
    return {'status': 'completed', 'output': response}