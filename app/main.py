from fastapi import FastAPI
import subprocess
from typing import Dict, Any
import shlex
def ping(host: str) -> Dict[str, Any]:
    try:
        # Sanitize and escape the input
        host = shlex.quote(host)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}