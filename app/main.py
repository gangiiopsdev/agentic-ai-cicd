from fastapi import FastAPI
import subprocess
from typing import Dict, Any

app = FastAPI()

def ping(host: str) -> Dict[str, Any]:
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}