from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call and avoiding shell=True
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'output': e.output}