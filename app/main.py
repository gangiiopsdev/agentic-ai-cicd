from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host parameter to ensure it only contains valid characters
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            return {'error': 'Invalid input'}, 400
        subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500