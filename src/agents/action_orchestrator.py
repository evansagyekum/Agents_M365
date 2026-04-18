import os
import requests
import json
import logging
import time
from azure.data.tables import TableClient

def main(decision_payload):
    # 1. Audit Log to Table Storage
    table_client = TableClient.from_connection_string(os.getenv("STORAGE_CONN"), "IncidentLogs")
    log_entry = {
        "PartitionKey": decision_payload['asset_id'],
        "RowKey": str(time.time()),
        "ActionCode": decision_payload['action_code'],
        "Rationale": decision_payload['explanation']
    }
    table_client.create_entity(entity=log_entry)

    # 2. Trigger Power Automate Flow
    PA_URL = os.getenv("POWER_AUTOMATE_WEBHOOK_URL")
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(PA_URL, data=json.dumps(decision_payload), headers=headers)
    
    if response.status_code == 202:
        logging.info("Workflow successfully triggered.")
    else:
        logging.error(f"Workflow trigger failed: {response.text}")
