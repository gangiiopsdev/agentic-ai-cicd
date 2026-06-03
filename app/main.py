from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if len(args) > 1 and ' '.join(args[1:]) != shlex.quote(' '.join(args[1:])):
        raise ValueError('Potential shell injection detected')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}