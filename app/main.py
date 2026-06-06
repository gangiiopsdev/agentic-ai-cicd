from fastapi import FastAPI
import subprocess
import shlex
import os

class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        if not isinstance(command, list):
            command = shlex.split(command)
        for key, value in kwargs.items():
            if key == 'cwd':
                if not os.path.exists(value):
                    raise ValueError(f"Directory {value} does not exist")
            elif key == 'env':
                for k, v in value.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        raise TypeError(f"Environment variable key and value must be strings")
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        command = ['ping', shlex.quote(host)]
        result = SafeSubprocess.safe_run(' '.join(command), shell=True, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}