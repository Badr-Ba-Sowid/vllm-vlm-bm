#!/bin/bash

python vllm-vlm-bm/benchmarks/benchmark_serving.py \
    --backend "openai-chat" \
    --model  "/media/akk/hdd3/hf_model/Qwen/Qwen2-VL-7B-Instruct"\
    --dataset-name sharegpt \
    --dataset-path "/home/akk/brada/mmvet_v2.json" \
    --num-prompts 1 