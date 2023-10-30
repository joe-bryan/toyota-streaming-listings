import json
import pandas as pd
import boto3

# Open JSON from Parquet Gzip compression file
df = pd.read_parquet("toyota_listings_100.parquet.gzip", engine="pyarrow")
df = df.to_dict(orient="records")

# Create a kinesis client
kinesis_client = boto3.client("kinesis", region_name="us-east-2")

counter = 0

for listing_event in df:
    # Send message to Kinesis data stream
    response = kinesis_client.put_record(
        StreamName="toyota-data-stream-developing",
        Data=json.dumps(listing_event),
        PartitionKey=str(hash(listing_event["event_time"])),
    )

    counter = counter + 1

    print("Message sent #" + str(counter))

    # If the message was not sucessfully sent, print an error message
    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
        print("Error!")
        print(response)
