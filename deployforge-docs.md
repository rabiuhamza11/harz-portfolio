# DeployForge v6.0 — Documentation

## Overview
DeployForge is a multi-cloud deployment platform built for the HARZ ecosystem. It allows you to deploy web applications, serverless functions, and Docker containers to multiple cloud providers — all from a single interface.

## Supported Runtimes

### 1. Static HTML → GitHub Pages (Free)
- Push any HTML file to your GitHub repository
- Auto-deploys via GitHub Actions on every push to main
- Live URL: `https://rabiuhamza11.github.io/harz-portfolio/FILENAME.html`

### 2. Node.js → Vercel (Free Serverless)
- Deploy serverless functions as API endpoints
- Auto-scales globally
- Live URL: `https://yourproject.vercel.app/api/handler`
- Free tier: 100GB bandwidth, 100k invocations/month

### 3. Python → Vercel (Free Serverless)
- Deploy Python functions as API endpoints
- Same Vercel infrastructure
- Free tier same as Node.js

### 4. Docker → Railway (Free 500hrs)
- Deploy any Docker image (nginx, node, python, postgres, redis, mongo)
- Railway auto-builds and runs your container
- One-click deploy from dashboard
- Free: 500 hours/month on Hobby plan

### 5. Cloudflare Workers (Pending Token)
- Deploy edge functions globally
- Sub-millisecond response times
- Requires CF_API_TOKEN and CLOUDFLARE_ACCOUNT_ID

## HARZ Templates (9)

| Template | Runtime | Description |
|----------|---------|-------------|
| HARZ Construction | HTML | Project tracking, cost estimation, material management |
| EstateHub | HTML | Property listings, tenant management, rent tracking |
| BuildBot AI | Node.js | AI construction cost calculator with material estimates |
| Danfodio School Portal | HTML | Student results, attendance, exam grading, fees |
| HARZ Farm Manager | HTML | Crop tracking, livestock, expenses, harvest schedule |
| HarzDM Marketplace | HTML | Product listings, cart, checkout, payment integration |
| HarzPay Gateway | HTML | Payment processing with Paystack, bank transfer, USDT |
| API Backend | Node.js | REST API with auth, CRUD, and database |
| Docker Container | Docker | Deploy any Docker image to Railway |

## CI/CD Pipelines

### Available Pipelines
1. **GitHub Pages** — Auto-deploy on push to main
2. **Vercel** — Auto-deploy on API changes
3. **Railway** — Auto-deploy on push
4. **Multi-Cloud** — Deploy to all platforms simultaneously

### Setup
1. Go to CI/CD tab
2. Select repository
3. Click the pipeline type you want
4. DeployForge creates the GitHub Actions workflow file automatically
5. Every push to main triggers the pipeline

## Monitoring
- Real-time HTTP status checking
- Latency tracking (milliseconds)
- Auto-refresh every 60 seconds
- LIVE/DOWN badges for instant visibility

## HarzPay Integration
- Paystack checkout for premium deployments
- Bank transfer support
- USDT (crypto) support
- Transaction verification

### Setup
1. Set `PAYSTACK_SECRET_KEY` in secrets
2. Use `harzpay_init` action to create checkout
3. Use `harzpay_verify` to verify payment

## Collaboration
- GitHub Issues integration (create and list)
- Team-based access control via GitHub Teams
- Pull request workflow for code review

## API Actions
All actions are available via POST to the backend function:

### GitHub
- `list_repos` — List all repositories
- `deploy_file` — Deploy a file to GitHub
- `create_repo` — Create a new repository
- `list_files` — List files in a repo
- `delete_file` — Delete a file from a repo

### CI/CD
- `cicd_create` — Create a CI/CD pipeline
- `cicd_status` — Check pipeline run status

### Vercel
- `vercel_list` — List Vercel projects
- `vercel_deploy` — Deploy to Vercel
- `vercel_delete` — Delete a Vercel project

### Railway
- `railway_docker_deploy` — Deploy Docker to Railway
- `railway_delete_project` — Delete Railway project

### Cloudflare
- `cloudflare_deploy` — Deploy to Cloudflare Workers

### Templates
- `template_list` — List all templates
- `template_get` — Get template code

### Monitoring
- `monitor` — Check URL status and latency

### Secrets
- `secrets_list` — List GitHub Actions secrets

### Issues
- `create_issue` — Create a GitHub issue
- `list_issues` — List GitHub issues

### HarzPay
- `harzpay_init` — Initialize Paystack payment
- `harzpay_verify` — Verify payment status

## Cost Comparison

| Platform | Monthly Cost | Free Tier |
|----------|-------------|-----------|
| DeployForge | ₦0 | All features free |
| Render Starter | $7 (~₦11,200) | Limited |
| Vercel Pro | $20 (~₦32,000) | 100GB bandwidth |
| Railway Hobby | $5 (~₦8,000) | 500 hours free |

## Architecture
- **Backend**: Base44 serverless function (deployForgeDeploy)
- **Frontend**: Single HTML file deployed to GitHub Pages
- **Storage**: GitHub repository for templates and deployments
- **Cloud Providers**: GitHub Pages, Vercel, Railway, Cloudflare
- **Payment**: Paystack via HarzPay integration
