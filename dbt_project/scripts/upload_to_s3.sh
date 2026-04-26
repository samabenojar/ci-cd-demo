#!/bin/bash

BUCKET_NAME=$1

if [ -z "$BUCKET_NAME" ]; then
    echo "Usage: ./scripts/upload_to_s3.sh your-bucket-name"
    exit 1
fi

aws s3 cp exports/fct_orders.csv s3://$BUCKET_NAME/exports/fct_orders.csv

echo "Upload complete"