# Construction AI Container

This Dockerized project runs:
1. YOLOv5 object detection on an input image (`input.jpg`)
2. LLM-based extraction of structured data from a text file (`construction_spec.txt`)

## How to Build
bash

docker build -t construction-ai .
docker run --rm -v "$(pwd):/app" construction-ai

