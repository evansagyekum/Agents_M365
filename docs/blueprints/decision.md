# Decision-Making AI Agent: Production Blueprint

This blueprint details the reasoning logic, safety guardrails, and prompt engineering required for a "High-Confidence" Decision Agent on Azure.

## 1. Multi-Scenario Reasoning Architecture

```mermaid
graph TD
    A[Alert Payload] --> B{Scenario Detection}
    B -- "Manufacturing" --> C[Operational Efficiency Logic]
    B -- "Chemical Plant" --> D[Safety-Critical Risk Logic]
    
    subgraph "Reasoning Core"
        C --> E[Reasoning Engine: GPT-4o]
        D --> E
        E --> F[5-Whys Analysis]
        E --> G[Risk Matrix Scoring]
    end
```

---

## 2. Refined Master Prompt Template (Excerpt)

# Safety Logic & Guardrails (Chemical Plant)
- **Rule 1**: If RUL < 12 hours AND Temperature is rising, recommend 'SHUTDOWN'.
- **Rule 2**: If Pressure > 90% of Rated Limit, trigger 'EMERGENCY_VENT'.
- **Rule 3**: Never suggest a maintenance action that involves opening a pressurized vessel without confirming 'DEPRESSURIZATION_COMPLETE'.
