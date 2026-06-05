from fastapi import FastAPI
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}