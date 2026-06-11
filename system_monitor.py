import boto3
import psutil
import datetime
import subprocess
import json
import os

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("================================")
print("Health Check v2: " + now)
print("================================")

# CPU — psutil reads directly from kernel
cpu_percent = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
print("CPU Usage: " + str(cpu_percent) + "% (" + str(cpu_count) + " cores)")

# Memory
mem = psutil.virtual_memory()
mem_total = round(mem.total / (1024**3), 1)
mem_used = round(mem.used / (1024**3), 1)
mem_percent = mem.percent
print("Memory: " + str(mem_used) + "GB used of " + str(mem_total) + "GB (" + str(mem_percent) + "%)")

# Disk
disk = psutil.disk_usage('/')
disk_total = round(disk.total / (1024**3), 1)
disk_used = round(disk.used / (1024**3), 1)
disk_percent = disk.percent
print("Disk: " + str(disk_used) + "GB used of " + str(disk_total) + "GB (" + str(disk_percent) + "%)")

# Apache
def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

apache = run_command("systemctl is-active apache2")

# Network bytes sent/received
net = psutil.net_io_counters()
mb_sent = round(net.bytes_sent / (1024**2), 1)
mb_recv = round(net.bytes_recv / (1024**2), 1)
print("Network: Sent " + str(mb_sent) + "MB / Received " + str(mb_recv) + "MB")


# Alerts
print("")
print("--- Alerts ---")

if cpu_percent > 80:
    print(RED + "WARNING: CPU is high! " + str(cpu_percent) + "%" + RESET)
elif cpu_percent > 50:
    print(YELLOW + "NOTICE: CPU is moderate " + str(cpu_percent) + "%" + RESET)
else:
    print(GREEN + "OK: CPU normal" + RESET)

if mem_percent > 80:
    print(RED + "WARNING: Memory is high! " + str(mem_percent) + "%" + RESET)
elif mem_percent > 60:
    print(YELLOW + "NOTICE: Memory is moderate " + str(mem_percent) + "%" + RESET)
else:
    print(GREEN + "OK: Memory normal" + RESET)

if disk_percent > 80:
    print(RED + "WARNING: Disk is high! " + str(disk_percent) + "%" + RESET)
elif disk_percent > 60:
    print(YELLOW + "NOTICE: Disk getting full " + str(disk_percent) + "%" + RESET)
else:
    print(GREEN + "OK: Disk normal" + RESET)

if apache != "active":
    print(RED +  "CRITICAL: Apache is DOWN!" + RESET)
else:
    print(GREEN + "OK: Apache running" + RESET)

print("")

# Build alerts list
alerts = []
if cpu_percent > 80:
    alerts.append("CPU HIGH: " + str(cpu_percent) + "%")
if mem_percent > 80:
    alerts.append("MEMORY HIGH: " + str(mem_percent) + "%")
if disk_percent > 80:
    alerts.append("DISK HIGH: " + str(disk_percent) + "%")
if apache != "active":
    alerts.append("APACHE DOWN")

# Build JSON entry
entry = {
    "timestamp": now,
    "cpu_percent": cpu_percent,
    "cpu_cores": cpu_count,
    "memory_used_gb": round(mem_used, 1),
    "memory_total_gb": round(mem_total, 1),
    "memory_percent": mem_percent,
    "disk_used_gb": round(disk_used, 1),
    "disk_total_gb": round(disk_total, 1),
    "disk_percent": disk_percent,
    "network_sent_mb": mb_sent,
    "network_recv_mb": mb_recv,
    "apache_status": apache,
    "alerts": alerts
}

# Load existing log or start fresh
log_file = os.path.expanduser("~/cloud_journey/health_log.json")

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        log_data = json.load(f)
else:
    log_data = []

# Append new entry and save
log_data.append(entry)
with open(log_file, "w") as f:
    json.dump(log_data, f, indent=2)

print("Log saved: " + log_file)

s3 = boto3.client('s3')
bucket_name = "jnthn-cloud-journey-2026"

try:
  s3.upload_file(log_file, bucket_name, "health_log.json")
  print(GREEN + "Uploaded to S3: " + bucket_name + RESET)

except Exception as e:
  print(RED + "S3 upload failed: " + str(e) + RESET)


print("================================")
