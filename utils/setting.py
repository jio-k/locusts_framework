import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_PATH = os.path.join(BASE_PATH, 'locusts_framework', 'data')

LOCUSTS_FRAMEWORK_PATH = os.path.join(BASE_PATH, 'locusts_framework')

REPORT_PATH = os.path.join(BASE_PATH, 'locusts_framework', 'report')

CASE_PATH = os.path.join(BASE_PATH, 'locusts_framework', 'scripts')

LOCUST_CFG_PATH = os.path.join(DATA_PATH, "locust.json")
