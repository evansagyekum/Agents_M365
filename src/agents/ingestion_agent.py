import time
import json
import random
import pandas as pd
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

# Configuration
CONN_STR = "HostName=YOUR_HUB.azure-devices.net;DeviceId=REACTOR-001;SharedAccessKey=xxx"

class IngestionAgent:
    def __init__(self, mode="simulate"):
        self.mode = mode
        if self.mode == "simulate":
            self.client = IoTHubDeviceClient.create_from_connection_string(CONN_STR)

    def generate_telemetry(self):
        """Creates realistic sensor data with random noise."""
        return {
            "temperature": round(random.uniform(150, 200), 2),
            "pressure": round(random.uniform(10, 15), 2),
            "vibration": round(random.uniform(0.01, 0.08), 3),
            "flow_rate": round(random.uniform(200, 300), 2)
        }

    def start_streaming(self, interval=5):
        """Starts real-time simulation."""
        print(f"Starting Streaming Agent on Reactor-001...")
        try:
            while True:
                data = self.generate_telemetry()
                msg = Message(json.dumps({
                    "header": {
                        "msg_id": str(random.randint(1000, 9999)),
                        "timestamp": datetime.utcnow().isoformat(),
                        "device_id": "REACTOR-001"
                    },
                    "payload": data
                }))
                self.client.send_message(msg)
                print(f"Sent: {data}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopping agent...")

    def process_batch(self, file_path):
        """Read a historical dataset and mock upload to ADLS Gen2."""
        print(f"Processing Batch File: {file_path}")
        df = pd.read_csv(file_path)
        df['ingested_at'] = datetime.utcnow()
        print(f"Detected {len(df)} rows. Partitioning by date...")
        print("Upload to ADLS Gen2 Successful.")

if __name__ == "__main__":
    agent = IngestionAgent(mode="simulate")
    agent.start_streaming(interval=10)
