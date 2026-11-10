import json
import sys

from awsip import (
    count_ip_range,
    download_aws_ip_set,
    find_ip,
    trouver_dernier_ip,
    trouver_premier_ip,
)

print(f"La première ip :{trouver_premier_ip()}")
print(f"La dernière ip :{trouver_dernier_ip()}")
print(f"Nb total d'ip : {count_ip_range()}")

match len(sys.argv):
    case 2:
        print(json.dumps(find_ip(download_aws_ip_set(), sys.argv[1]), indent=2))
    case _:
        pass
