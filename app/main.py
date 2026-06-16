from fastapi import FastAPI
import subprocess
from shlex import quote

class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            quoted_host = quote(host)
            result = subprocess.run(['ping', quoted_host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e}

app = FastAPI()

def ping(host: str):
    safe_ping_instance = SafePing()
    return {'status': 'completed', 'result': safe_ping_instance.safe_ping(host)}