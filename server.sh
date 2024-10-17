  #!/bin/bash

  vllm serve "/media/akk/hdd3/hf_model/Qwen/Qwen2-VL-7B-Instruct" \
        --swap-space 16 \
        --disable-log-requests
