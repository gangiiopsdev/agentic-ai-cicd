from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c 1', quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {str(e)}'
    except Exception as e:
        return f'Error: {str(e)}'
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'success', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}