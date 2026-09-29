# Team Task Board: Course Project

This is the one small application used throughout the course. You do not need to write the starter code before learning DevOps. Read it, run it, then use the module labs to package, test, observe, and release it.

## What it does?

The page lets one learner add, complete, and remove tasks. Tasks are saved in that browser's local storage, so they stay on that device/browser only; this is a learning demo, not a shared production task system. A tiny Python web server serves the page and exposes `/health` and `/metrics` endpoints. It writes request information to standard output so a container platform can collect the logs.

## Run locally

1. Install Python 3.11 or later.
2. Open a terminal at the course repository root.
3. Run the automated checks: `python -m unittest discover -s project/tests`.
4. Start the app: `python project/app/app.py`.
5. Open `http://localhost:8080/`. In another tab, check `http://localhost:8080/health` and `http://localhost:8080/metrics`.
6. Stop the server with Ctrl+C.

PowerShell users can use `Invoke-WebRequest http://localhost:8080/health`; Bash users can use `curl http://localhost:8080/health`.

## Project path through the course

- Git and GitHub: put the course project under version control and review each change in a pull request.
- Terraform: create a private release bucket and learn to review infrastructure changes safely.
- CloudFormation: model a task-event queue and dead-letter queue as a separate AWS stack.
- Docker and Kubernetes: build the project image, push it to ECR, and run it in local `kind`.
- Prometheus and Grafana: scrape the app's request counter and graph its rate.
- CloudWatch Logs: create a log destination and query sample application events.
- AWS networking and security: design the VPC and identity boundaries that a future hosted version would need.
- CI/CD: test the project on pull requests and publish the same page as a commit-specific private release artifact using GitHub OIDC.

The AWS examples remain small, isolated learning environments so you can clean them up after each lab. The capstone connects the ideas; it does not require running a costly always-on cluster.

The Terraform and CloudFormation examples create separate disposable resources for their own labs. The capstone may combine or reuse resources only after learners understand ownership, naming, access, state, cost, and cleanup. Do not run two provisioning tools against the same resource.
