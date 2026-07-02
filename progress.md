# Cloud Engineer Journey — gloki

## Day 1 
- Explored system info (uname, df, free, ps, ip addr)
- Learned Linux service management (systemctl)
- Discovered Apache2 and LXC already installed

## Day 2 
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

## Day 7 — (EC2 Deployed)
- Ran the full pipeline end to end.
- took a refresher quiz about everything so far hahaha

## Day 8 - (Deployed the monitor to cloud)
- Created key pair for SSH access
- Created security group (ports 22, 80 open)
- Launched t3.micro EC2 instance (free tier)
- SSH'd into real cloud server in Singapore
- Created IAM Role (cloud-journey-ec2-role) with S3 access
- Attached IAM role to EC2 - no keys stored on server!
- Cloned GitHub repo onto EC2
- Deployed system_monitor.py to EC2
- Automated with cron (runs every hour)
- Learned: least privilege principle in action

## Day 9 - Apache on EC2, web dashboard, User Data scripts
- Install apache on ec2
- created a dashboard for system_monitor.py
- dashboard live at public ip
- Auto-refreshes every 60 seconds in browser
- Updated CRON to run monitor + dashboard together every hour
- Transferred the dashboard to laptop via scp
- Learned: f-strings, negative indexing log_data[-1], scp file transfer


## Day 10 
- Installed Terraform v1.15.6
- Created variables.tf, main.tf, outputs.tf
- Learned: provider, resource, variables, outputs, tags
- terraform init → plan → apply → destroy
- Deployed 2 resources (EC2 + Security Group) with one command
- Learned: .tfstate file, (known after apply), ManagedBy tags

## Day 11 
- Created user_data.sh — server auto-configures on boot
- Added IAM Role + Policy + Instance Profile to Terraform
- Full 5-resource stack deployed with terraform apply
- Server self-configured: Apache, Python, boto3, repo clone, cron
- Dashboard live automatically — zero manual SSH steps
- Fixed log file path bug — committed to GitHub
- Clean terraform destroy — all 5 resources removed

## Next: Day 12 — GitHub Actions CI/CD pipeline
- Created .github/workflows/deploy.yml
- Set up GitHub Secrets (EC2_HOST, EC2_SSH_KEY)
- CI/CD pipeline auto-deploys on every git push to main
- Fixed merge conflict — git reset --hard in deploy script
- Added health_log.json to .gitignore
- Tested end-to-end: push code → dashboard auto-updates
- Learned: YAML, GitHub Actions, workflows, secrets, CI/CD concepts

## Next: Day 13 — AWS Cloud Practitioner exam prep
- Studied all 4 CLF-C02 exam domains
- Cloud Concepts: 6 benefits, IaaS/PaaS/SaaS, deployment models
- Security: Shared Responsibility Model, IAM concepts, security services
- Technology: Compute, Storage, Networking, Database services
- Billing: Pricing models, billing tools, support plans, global infrastructure
- Quiz score: 11/12 (92%)
- Weak area: IaaS vs PaaS distinction
- Next: AWS Skill Builder course + practice exams
- added EIP/ Dont forget to release the eip when EC2 stopped long-term
 
## Next: Day 14 — Week 2 review + mock interview questions
Completed full mock interview session
- Refined elevator pitch — natural and technical
- Practiced 5 interview questions
- Overall score: 9.2/10
- Strong areas: IAM explanation, CI/CD debugging story, 2-year plan
- Area to improve: Debug scenarios — think network→service→app→data
- Key lesson: Specific details = credibility in interviews
