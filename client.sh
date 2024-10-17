#!/bin/bash

python benchmarks/benchmark_serving.py \
    --backend "openai-chat" \
    --model  <your model path> \
    --dataset-name sharegpt \
    --dataset-path  <your dataset path>  \
    --num-prompts 1 