# Databricks Asset Bundle - Medallion Architecture Pipeline

A production-ready Databricks Asset Bundle implementing the medallion architecture (Bronze, Silver, Gold) for data pipeline orchestration.

## 🏗️ Project Structure

```
github-copilot/
├── databricks.yml                  # Main bundle configuration with environments
├── .github/
│   └── workflows/
│       └── databricks-deploy.yml   # CI/CD pipeline for validation and deployment
├── resources/
│   └── workflow.yml                # Databricks job/workflow definitions
├── src/
│   ├── bronze.py                   # Bronze layer - raw data ingestion
│   ├── silver.py                   # Silver layer - data transformation
│   └── gold.py                     # Gold layer - business aggregations
├── setup.py                        # Python package configuration
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 📋 Prerequisites

- **Databricks Workspace** (Azure Databricks, AWS Databricks, or GCP Databricks)
- **Databricks CLI** installed locally
- **Personal Access Token** for both pre-prod and production environments
- **Python 3.8+** installed
- **Git** for version control

## 🔧 Configuration Required

Before deploying, you need to update the following placeholders with your actual values:

### 1. databricks.yml

Replace these placeholders:
- `YOUR_PRE_PROD_DATABRICKS_WORKSPACE_URL` - Your pre-production Databricks workspace URL
- `YOUR_PRE_PROD_DATABRICKS_ACCESS_TOKEN` - Personal access token for pre-prod
- `YOUR_PROD_DATABRICKS_WORKSPACE_URL` - Your production Databricks workspace URL
- `YOUR_PROD_DATABRICKS_ACCESS_TOKEN` - Personal access token for production
- `YOUR_PRODUCTION_SERVICE_PRINCIPAL_NAME` - Service principal for production runs

### 2. resources/workflow.yml

Replace these placeholders:
- `YOUR_EMAIL_ADDRESS_FOR_JOB_START_NOTIFICATIONS` - Email for job start alerts
- `YOUR_EMAIL_ADDRESS_FOR_JOB_SUCCESS_NOTIFICATIONS` - Email for success alerts
- `YOUR_EMAIL_ADDRESS_FOR_JOB_FAILURE_NOTIFICATIONS` - Email for failure alerts
- `YOUR_DATABRICKS_NODE_TYPE_ID` - Node type (e.g., `Standard_DS3_v2`, `i3.xlarge`)

### 3. src/bronze.py

Replace these placeholders:
- `YOUR_SOURCE_DATA_PATH_1` - Path to your source data (e.g., s3://bucket/data/)
- `YOUR_SOURCE_DATA_PATH_2` - Path to your second data source

### 4. GitHub Secrets (for CI/CD)

Add these secrets to your GitHub repository:
- `PRE_PROD_DATABRICKS_HOST` - Pre-prod workspace URL
- `PRE_PROD_DATABRICKS_TOKEN` - Pre-prod access token
- `PROD_DATABRICKS_HOST` - Production workspace URL
- `PROD_DATABRICKS_TOKEN` - Production access token

## 🚀 Quick Start

### 1. Install Databricks CLI

```bash
# Install the Databricks CLI
pip install databricks-cli

# Or use the installer
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
```

### 2. Configure Authentication

```bash
# Configure for pre-prod
databricks configure --token

# Enter your workspace URL and token when prompted
```

### 3. Validate the Bundle

```bash
# Validate the bundle configuration
databricks bundle validate -t pre_prod
```

### 4. Deploy to Pre-Production

```bash
# Deploy to pre-production environment
databricks bundle deploy -t pre_prod
```

### 5. Run the Pipeline

```bash
# Run the deployed job
databricks bundle run -t pre_prod data_pipeline_job
```

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow that automatically:

1. **Validates** the bundle on every pull request
2. **Deploys to pre-prod** when code is merged to `develop` branch
3. **Deploys to production** when code is merged to `main` branch

### Workflow Triggers

- **Push to `develop`** → Deploy to pre-prod
- **Push to `main`** → Deploy to production
- **Pull Request** → Validate only
- **Manual Trigger** → Deploy to selected environment

## 📊 Data Pipeline Architecture

### Bronze Layer (Raw)
- **Purpose**: Ingest raw data from source systems
- **File**: `src/bronze.py`
- **Operations**:
  - Read data from various sources (S3, ADLS, etc.)
  - Add metadata columns (ingestion timestamp, source file)
  - Store in Delta format with minimal transformations

### Silver Layer (Cleansed)
- **Purpose**: Clean, validate, and standardize data
- **File**: `src/silver.py`
- **Operations**:
  - Data quality checks
  - Remove duplicates
  - Standardize formats
  - Handle missing values
  - Business rule validation

### Gold Layer (Curated)
- **Purpose**: Create business-level aggregations
- **File**: `src/gold.py`
- **Operations**:
  - Customer analytics (RFM analysis, lifetime value)
  - Sales metrics (daily, monthly aggregations)
  - Dimension tables for star schema
  - KPIs and business metrics

## 🛠️ Local Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests Locally

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v --cov=src
```

### Sync Files to Workspace

```bash
# Sync your local files to Databricks workspace
databricks bundle sync -t pre_prod
```

## 📝 Common Commands

```bash
# Validate bundle
databricks bundle validate -t pre_prod

# Deploy bundle
databricks bundle deploy -t pre_prod

# Run a specific job
databricks bundle run -t pre_prod data_pipeline_job

# Destroy deployed resources
databricks bundle destroy -t pre_prod

# View bundle summary
databricks bundle summary -t pre_prod
```

## 🔐 Security Best Practices

1. **Never commit tokens** to version control
2. Use **service principals** for production deployments
3. Store secrets in **GitHub Secrets** or **Azure Key Vault**
4. Implement **least privilege** access controls
5. Regularly **rotate credentials**
6. Enable **audit logging** in Databricks

## 📈 Monitoring and Observability

- Job execution logs available in Databricks workspace
- Email notifications configured for job status
- Monitor cluster utilization and costs
- Set up alerts for job failures

## 🤝 Contributing

1. Create a feature branch from `develop`
2. Make your changes
3. Run validation: `databricks bundle validate`
4. Submit a pull request
5. CI/CD will automatically validate your changes

## 📞 Support

For issues or questions:
- Check Databricks documentation: https://docs.databricks.com/
- Review bundle reference: https://docs.databricks.com/dev-tools/bundles/

## 📄 License

Internal use only - Proprietary

---

**Last Updated**: April 2026
