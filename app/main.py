from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in '.:-' for c in host):
            raise HTTPException(status_code=400, detail='Invalid hostname provided')
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except TimeoutExpired:
        return {'status': 'timed out'}