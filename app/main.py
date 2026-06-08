from fastapi import FastAPI
import subprocess
cmd = ['ping', '-c', '1', host]
for arg in cmd:
    if not isinstance(arg, str) or '&&' in arg or ';' in arg or '||' in arg:
        raise ValueError('Invalid command argument')
subprocess.run(cmd, check=True, capture_output=True)
return {"status": "completed"}