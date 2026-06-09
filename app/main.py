from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output, error = execute_ping(host)
        if error:
            return {'status': 'error', 'output': error}
        else:
            return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}