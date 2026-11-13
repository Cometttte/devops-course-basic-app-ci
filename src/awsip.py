import ipaddress
import json
import ssl
import urllib.request


def download_aws_ip_set():
  """Downloads the AWS IP range JSON file and returns it as a dictionary."""

  # URL of the AWS IP range JSON file
  aws_ip_range_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

  # Download the JSON file
  ssl_context = ssl.create_default_context()
  ssl_context.check_hostname = False
  ssl_context.verify_mode = ssl.CERT_NONE
  with urllib.request.urlopen(aws_ip_range_url, context=ssl_context) as url:
    aws_ip_range_data = json.load(url)

  return aws_ip_range_data['prefixes']

# Find ip given IP belongs to any AWS Service
def find_ip(ip_range_data, ip_to_find):
  """Finds the AWS IP range that contains the given IP address."""
  return [prefix for prefix in ip_range_data if ipaddress.ip_address(ip_to_find) in ipaddress.ip_network(prefix['ip_prefix'])]

def find_aws_ip(ip_to_find):
  return find_ip(download_aws_ip_set(), ip_to_find)

def trouver_premier_ip():
  """Finds the first IP address in the AWS IP range JSON file."""
  ip_range_data = download_aws_ip_set()
  return ip_range_data[0]['ip_prefix'] if ip_range_data else None

def trouver_dernier_ip():
  """Finds the first IP address in the AWS IP range JSON file."""
  ip_range_data = download_aws_ip_set()
  return ip_range_data[-1]['ip_prefix'] if ip_range_data else None

def count_ip_range():
  ip_range_data = download_aws_ip_set();
  return len(ip_range_data) - 1 
  
