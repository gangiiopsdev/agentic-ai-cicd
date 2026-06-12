from fastapi import FastAPI, HTTPException
import subprocess
class ValidationError(Exception):
    pass

app = FastAPI()

@app.get("/{host:path}")
def ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValidationError('Invalid characters in host name. Only alphanumeric, dots, hyphens, and underscores are allowed.')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValidationError as e:
        return {'status': 'invalid', 'error': str(e)}