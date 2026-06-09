from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    for arg in args:
        if not isinstance(arg, str) or not all(c.isalnum() or c in '._-' for c in arg):  # Simple validation
            return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(args, check=True)
    return {'status': 'completed'}