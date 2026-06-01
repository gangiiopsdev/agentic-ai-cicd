from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper quoting of arguments to mitigate shell injection risk
    command = ['ping', host]
    quoted_command = ' '.join(shlex.quote(arg) for arg in command)
    try:
        output = subprocess.check_output(quoted_command, stderr=subprocess.STDOUT, timeout=5, shell=True)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}