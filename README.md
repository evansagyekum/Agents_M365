# Industrial Multi-Agent System for Predictive Maintenance

This project designs and prototypes a production-grade, multi-agent AI system for predictive maintenance in industrial environments, with a specific focus on chemical plant safety and equipment reliability.

## Architecture Highlights
- **Azure IoT Edge & Hub**: Real-time sensor data ingestion.
- **Azure Machine Learning**: RUL (Remaining Useful Life) and anomaly detection using the NASA Turbofan dataset.
- **Azure AI Foundry**: Decision-making agent with safety-critical reasoning and RAG integration for technical manuals.
- **Microsoft 365 Integration**: Automated workflows via **Power Automate**, interactive alerting in **Microsoft Teams**, and maintenance ticketing in **SharePoint Lists**.
- **Power BI Dashboards**: Real-time operational visibility, safety KPI tracking, and fleet health heatmaps.

## Repository Structure
- **`docs/blueprints/`**: Detailed technical design documents for each agent and the overall architecture.
- **`src/agents/`**: Prototype implementation code for data ingestion, ML pipelines, and action orchestration.

## Getting Started
1. Review the blueprints in `docs/blueprints/` to understand the system flow and safety guardrails.
2. The prototype agents in `src/agents/` require Azure SDKs for Python and an active Azure tenant with IoT Hub, Azure AI Foundry, and Microsoft 365 connectors configured.
