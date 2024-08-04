from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from prompt import prompts, system_message


access_token = ""

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    token=access_token
)

model_conclusions = []

for prompt in prompts:
    # Combine the system message and user prompt
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("")
    ]

    outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
        )

    response = outputs[0][input_ids.shape[-1]:]
    decoded_response = tokenizer.decode(response, skip_special_tokens=True)
  
    model_conclusions.append(decoded_response)
