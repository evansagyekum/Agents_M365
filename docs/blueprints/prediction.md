# Prediction Agent: Technical Blueprint

This document details the machine learning implementation for predicting equipment Remaining Useful Life (RUL) and anomaly scores using the NASA C-MAPSS dataset.

## 1. Feature Engineering & Training Pipeline

This Python logic implements a piecewise-linear RUL strategy with rolling window features.
(See `src/agents/prediction_pipeline.py` for code).

---

## 2. Azure ML Deployment Specifications

### Deployment Endpoint (`endpoint.yml`)
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: pred-maintenance-api
auth_mode: key
description: Real-time RUL prediction for reactor mixing motors.
```

### Managed Online Deployment (`deployment.yml`)
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: production-v1
endpoint_name: pred-maintenance-api
model: azureml:turbofan_xgboost_model:1
instance_type: Standard_DS3_v2
instance_count: 1
environment_variables:
  ANOMALY_THRESHOLD: "0.75"
```
