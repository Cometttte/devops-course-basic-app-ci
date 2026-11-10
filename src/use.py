import sys
import json
from awsip import find_ip, download_aws_ip_set, count_ip_range

print(json.dumps(find_ip(download_aws_ip_set(), sys.argv[1]), indent=2))
print(f"Nb total d'ip : {count_ip_range()}")