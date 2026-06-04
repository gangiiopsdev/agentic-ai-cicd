from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    result = subprocess.run(['ping', f'"{host}"'], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}