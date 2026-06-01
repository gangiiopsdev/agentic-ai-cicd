from fastapi import FastAPI
import subprocess
global_args = ['ping', '--']
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = global_args + [host]
    try:
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}