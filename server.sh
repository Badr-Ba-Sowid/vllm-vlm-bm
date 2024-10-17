  #!/bin/bash

  vllm serve <your dataset path> \
        --swap-space 16 \
        --disable-log-requests
