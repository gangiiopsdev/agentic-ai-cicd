from fastapi import FastAPI
import shlex

def safe_subprocess(command):
    try:
        args = shlex.split(command)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()