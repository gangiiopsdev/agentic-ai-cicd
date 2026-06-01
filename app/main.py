from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    try:
        # Use os.path.realpath to sanitize the input
        sanitized_host = subprocess.run(['realpath', request.host], check=True, capture_output=True, text=True, shell=False).stdout.strip()
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.SubprocessError as e:
        return {'status': 'failed', 'error': str(e)}