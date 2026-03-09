import numpy as np
import pandas as pd
import cv2  # Imported for future computer vision features

def get_location():
    latitude = round(np.random.uniform(-90, 90), 4)
    longitude = round(np.random.uniform(-180, 180), 4)
    return f"{latitude}, {longitude}"

def send_alert(location):
    print(f"Alert! Emergency detected at {location}")
    # Log the alert to a CSV file
    log_df = pd.DataFrame({"Location": [location], "Status": ["Alert Sent"]})
    log_df.to_csv("alert_log.csv", mode='a', header=False, index=False)
    print("Alert logged to alert_log.csv")
