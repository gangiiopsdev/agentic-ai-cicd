from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'message': 'Ping successful', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return {'status': 'failed', 'message': 'Ping failed'}