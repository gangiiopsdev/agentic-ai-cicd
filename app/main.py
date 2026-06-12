from fastapi import FastAPI
import subprocess
def escape_user_input(user_input):
    return subprocess.list2cmdline([user_input])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', escape_user_input(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}