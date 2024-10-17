from PIL import Image
import io
import json
from typing import Any, List, Dict
import base64
from tqdm import tqdm

from datasets import DatasetDict, load_dataset

def format_image(image: Image) -> str:
    image = image.convert("RGB")
    image_data = io.BytesIO()
    image.save(image_data, format='JPEG')
    image_base64 = base64.b64encode(image_data.getvalue()).decode("utf-8")
    return image_base64

def to_sharegpt(dict_dataset: DatasetDict) -> List[Dict[str, Any]]:
    return[
        {
            "conversations":[
                {
                    "from": "human",
                    "value": example["question"]
                },
                {
                    "from": "assistant",
                    "value": example["answer"]
                }
            ],
            "mm_content": {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{format_image(example['image_0'])}"
                },
            }
        }
        for _, dataset in dict_dataset.items()
        for example in tqdm(dataset, desc="Formating dataset")
    ]


def to_json(data: Any, file_path: str):
      with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    dataset = load_dataset("whyu/mm-vet-v2")
    sharegpt_dataset = to_sharegpt(dataset)
    to_json(sharegpt_dataset, "/home/akk/brada/mmvet_v2.json")
if __name__ == "__main__":
    main()