import json
import os
from datetime import datetime

# Load health log
log_file = os.path.expanduser("~/cloud-engineering-journey/health_log.json")

with open(log_file, "r") as f:
    log_data = json.load(f)

# Get latest entry
latest = log_data[-1]

# Calculate averages
avg_cpu = round(sum(e["cpu_percent"] for e in log_data) / len(log_data), 1)
avg_mem = round(sum(e["memory_percent"] for e in log_data) / len(log_data), 1)

# Generate HTML

html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Cloud Journey Monitor</title>
    <meta http-equiv="refresh" content="60">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #1a1a2e;
            color: #eee;
            padding: 20px;
            margin: 0;
        }}
        h1 {{
            color: #00d4ff;
            text-align: center;
        }}
        .subtitle {{
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            max-width: 900px;
            margin: 0 auto;
        }}
        .card {{
            background: #16213e;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            border: 1px solid #0f3460;
        }}
        .card h2 {{
            font-size: 14px;
            color: #888;
            margin: 0 0 10px 0;
            text-transform: uppercase;
        }}
        .value {{
            font-size: 36px;
            font-weight: bold;
            color: #00d4ff;
        }}
        .ok {{ color: #00ff88; }}
        .warning {{ color: #ffaa00; }}
        .critical {{ color: #ff4444; }}
        .history {{
            max-width: 900px;
            margin: 30px auto;
            background: #16213e;
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #0f3460;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th {{
            color: #00d4ff;
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #0f3460;
        }}
        td {{
            padding: 8px;
            border-bottom: 1px solid #0f3460;
            font-size: 13px;
        }}
        .footer {{
            text-align: center;
            color: #555;
            margin-top: 20px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <h1>🖥️ Cloud Journey Monitor</h1>
    <p class="subtitle">EC2 Instance — ap-southeast-1 (Singapore) | Auto-refreshes every 60s</p>

    <div class="grid">
        <div class="card">
            <h2>CPU Usage</h2>
            <div class="value {'warning' if latest['cpu_percent'] > 50 else 'ok'}">{latest['cpu_percent']}%</div>
            <div>Avg: {avg_cpu}%</div>
        </div>
        <div class="card">
            <h2>Memory</h2>
            <div class="value {'warning' if latest['memory_percent'] > 60 else 'ok'}">{latest['memory_percent']}%</div>
            <div>{latest['memory_used_gb']}GB of {latest['memory_total_gb']}GB</div>
        </div>
        <div class="card">
            <h2>Disk</h2>
            <div class="value {'warning' if latest['disk_percent'] > 60 else 'ok'}">{latest['disk_percent']}%</div>
            <div>{latest['disk_used_gb']}GB of {latest['disk_total_gb']}GB</div>
        </div>
        <div class="card">
            <h2>Network Sent</h2>
            <div class="value ok">{latest['network_sent_mb']}MB</div>
        </div>
        <div class="card">
            <h2>Network Recv</h2>
            <div class="value ok">{latest['network_recv_mb']}MB</div>
        </div>
        <div class="card">
            <h2>Apache</h2>
            <div class="value {'ok' if latest['apache_status'] == 'active' else 'warning'}">{latest['apache_status'].upper()}</div>
        </div>
    </div>

    <div class="history">
        <h2 style="color:#00d4ff">📊 History ({len(log_data)} entries)</h2>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>CPU%</th>
                <th>Memory%</th>
                <th>Disk%</th>
                <th>Alerts</th>
            </tr>
"""

for entry in reversed(log_data[-10:]):
    alerts = ", ".join(entry["alerts"]) if entry["alerts"] else "none"
    html += f"""
            <tr>
                <td>{entry['timestamp']}</td>
                <td>{entry['cpu_percent']}%</td>
                <td>{entry['memory_percent']}%</td>
                <td>{entry['disk_percent']}%</td>
                <td>{alerts}</td>
            </tr>"""

html += f"""
        </table>
    </div>

    <div class="footer">
        Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC |
        jnthn-cloud | Cloud Engineering Journey
    </div>
</body>
</html>"""

# Save to Apache web folder
output_path = "/var/www/html/index.html"
with open(output_path, "w") as f:
    f.write(html)

print("Dashboard generated: " + output_path)
