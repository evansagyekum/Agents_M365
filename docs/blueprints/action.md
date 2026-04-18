# Action Agent: Technical Blueprint

This document details the final orchestration layer that translates AI decisions into business actions across the Microsoft 365 ecosystem.

## 1. Action Workflow Orchestration

```mermaid
graph TD
    DA[Decision Agent Payload] --> AF[Azure Function: Orchestrator]
    AF -- "Audit Log" --> ATS[Azure Table Storage]
    
    AF -- "POST to HTTP Trigger" --> PA[Power Automate Flow]
    
    subgraph "Microsoft 365 Integration"
        PA --> SPL[Create Ticket: SharePoint List]
        PA --> Teams[Post Adaptive Card: Teams Channel]
    end
```

---

## 2. Microsoft Teams: Adaptive Card JSON

```json
{
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "TextBlock",
      "text": "🚨 Predictive Maintenance Alert",
      "weight": "Bolder",
      "size": "Large",
      "color": "Attention"
    }
  ]
}
```
