#!/bin/bash

echo "Starting Streamlit app..."

streamlit run app.py \
  --server.port=8000 \
  --server.address=0.0.0.0