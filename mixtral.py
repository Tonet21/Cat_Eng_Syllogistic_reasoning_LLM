from transformers import AutoModelForCausalLM, AutoTokenizer
from prompt import prompts

acces_token = "<your HF access token>"

model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1", token=acces_token, device_map="auto")

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1", token=acces_token)

model_conclusions = []


for prompt in prompts:

    messages = [

    {"role": "user", "content": prompt},
    ]

    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")

    generated_ids = model.generate(model_inputs, max_new_tokens=100, do_sample=True)

    model_conclusion = tokenizer.batch_decode(generated_ids)[0]

    model_conclusions.append(model_conclusion)

