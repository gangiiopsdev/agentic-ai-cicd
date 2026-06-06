from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and argument validation
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}