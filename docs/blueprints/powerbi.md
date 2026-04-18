# Power BI Dashboard: Technical Blueprint

## 1. Data Model (Star Schema)

```mermaid
erDiagram
    FACT_TELEMETRY ||--o{ DIM_ASSETS : "Sensor Metrics"
    FACT_PREDICTIONS ||--o{ DIM_ASSETS : "AI Insights"
    FACT_MAINT_LOGS ||--o{ DIM_ASSETS : "History"
```

---

## 2. Core DAX Measures

### Asset Health Index (0-100)
```dax
HealthIndex = 
VAR AvgAnomaly = AVERAGE(Fact_Predictions[AnomalyScore])
RETURN (1 - AvgAnomaly) * 100
```
