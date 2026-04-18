# Data Ingestion Agent: Technical Blueprint

This document provides the implementation details for the first agent in our multi-agent predictive maintenance system.

## 1. Ingestion Architecture

```mermaid
graph LR
    subgraph "Data Sources"
        SIM[Simulated Sensors]
        REAL[CSV/Batch Datasets]
    end

    subgraph "Data Ingestion Agent (Python)"
        AGENT[Ingestion Controller]
        AGENT -- "Stream" --> PROTO[MQTT / AMQP]
        AGENT -- "Batch" --> BULK[Bulk Upload Utility]
    end

    subgraph "Azure Ingestion Services"
        PROTO --> IH[Azure IoT Hub]
        BULK --> ADLS[ADLS Gen2]
    end

    subgraph "Storage Layers"
        IH --> ASA[Stream Analytics]
        ASA --> ADX[Azure Data Explorer - Hot]
        ADLS --> SQL[Azure SQL - Metadata]
    end
```

---

## 2. Sample Schema Design

### A. JSON Telemetry (Streaming)
Used for real-time messages sent to IoT Hub.
```json
{
  "header": {
    "msg_id": "9821-abc-123",
    "timestamp": "2024-04-18T21:30:00Z",
    "device_id": "REACTOR-001"
  },
  "payload": {
    "temperature": 185.4,
    "pressure": 12.8,
    "vibration": 0.045,
    "flow_rate": 250.0
  },
  "status": "OPERATIONAL"
}
```
