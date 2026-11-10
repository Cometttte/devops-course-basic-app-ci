import sys
import json
from awsip import find_ip, download_aws_ip_set, trouver_premier_ip, trouver_dernier_ip

#sys.stdout.write(json.dumps(find_ip(download_aws_ip_set(), sys.argvpyhto[1]), indent=2))

print(f"La première ip :{trouver_premier_ip()}")
print(f"La dernière ip :{trouver_dernier_ip()}")