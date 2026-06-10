from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use check_output instead of call for better error handling and security
        output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}