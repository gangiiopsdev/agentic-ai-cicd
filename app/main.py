from fastapi import FastAPI
import subprocess
import shlex

cmd = ['ping', '-c', '1']
host_parts = host.split()
for part in host_parts:
    if not part.isnumeric() or len(part) > 15:
        return {'status': 'error', 'message': 'Invalid input'}
    cmd.append(shlex.quote(part))

subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
return {'status': 'completed'}