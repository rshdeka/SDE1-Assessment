import uuid
from process import process_csv

csv_filename = "Input.csv"
request_id = str(uuid.uuid4())

output_csv_path = process_csv(csv_filename, request_id)
print(f"Processed CSV saved at: {output_csv_path}")