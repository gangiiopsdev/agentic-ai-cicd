from fastapi import FastAPI
import re
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Union[dict, None]:
    # Validate the input to ensure it only contains allowed characters (alphanumeric, hyphen, dot)
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}