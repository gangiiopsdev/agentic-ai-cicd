from fastapi import FastAPI
import subprocess
call_command = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = call_command.communicate()
if call_command.returncode != 0:
    raise Exception(f"Ping failed with return code: {call_command.returncode}")
return {'status': 'completed'}