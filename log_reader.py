import json
import os


log_file = os.path.expanduser("~/cloud_journey/health_log.json")

with open(log_file, "r") as f:
    log_data = json.load(f)


total_entries = len(log_data)
print("================================")
print("Health Log Summary")
print("Total entries: " + str(total_entries))
print("================================")


for entry in log_data:
    print("")
    print("Time   : " + entry["timestamp"])
    print("CPU    : " + str(entry["cpu_percent"]) + "%")
    print("Memory : " + str(entry["memory_percent"]) + "%")
    print("Disk   : " + str(entry["disk_percent"]) + "%")
    print("Apache : " + entry["apache_status"])

    if len(entry["alerts"]) > 0:
        print("ALERTS : " + str(entry["alerts"]))
    else:
        print("Alerts : none")

print("")
print("================================")

avg_cpu = sum(e["cpu_percent"] for e in log_data) / total_entries
avg_mem = sum(e["memory_percent"] for e in log_data) / total_entries


print("Average CPU    : " + str(round(avg_cpu, 1)) + "%")
print("Average Memory : " + str(round(avg_mem, 1)) + "%")
print("================================")
