# Cloud Engineer Journey — gloki

## Day 1 ✅
- Explored system info (uname, df, free, ps, ip addr)
- Learned Linux service management (systemctl)
- Discovered Apache2 and LXC already installed

## Day 2 ✅
- Read Apache access logs
- Built system_health.sh monitoring script
- Debugged smart quotes and IPv6 issues
- Automated with cron (runs every hour)

## Files
- ~/system_health.sh — health monitor script
- ~/health_log.txt — running log output
- ~/cloud_journey/progress.md — this file

## Day 3 — Python Scripting
- Wrote first Python script (hello.py)
- Rewrote health monitor in Python (system_info.py)
- Built psutil-powered monitor with alerts (health_v2.py)
- Learned: imports, objects, functions, if/elif/else
- Fixed NameError bug — learned variable scope

## Files
- ~/cloud_journey/hello.py
- ~/cloud_journey/system_info.py
- ~/cloud_journey/health_v2.py

## Day 4 — Save logs to JSON + intro to boto3 (AWS SDK)
- Added colored terminal output with ANSI codes
- Built JSON logging system
- Built log_reader.py to query and analyze logs
- Learned: lists, dictionaries, for loops, file I/O, json module
- Fixed variable scope bug (mb_sent)

## Day 5 — AWS CLI setup + first cloud commands
- Created AWS account with zero-spend budget
- Installed AWS CLI v2
- Created IAM user (gloki-cli) - never use root
- Configured AWS CLI (region: ap-southeast-1)
- Verified connection with sts get-caller-identity
- Confirmed account clean: $0 resources

## Day 6 — First S3 bucket + upload health logs to cloud
- Created S3 bucket via AWS CLI
- Uploaded files to S3 (CLI + boto3)
- Integrated boto3 into system_monitor.py
- Script now auto-uploads JSON logs to cloud on every run
- Learned: boto3 client, try/except error handling

## Day 7 — (EC2 deployment)
