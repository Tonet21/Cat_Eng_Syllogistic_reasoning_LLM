from huggingface_hub import snapshot_download
from pathlib import Path
from mistral_inference.model import Transformer
from mistral_inference.generate import generate
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from prompt import prompts,system_message
from mistral_common.protocol.instruct.messages import SystemMessage


access_token = ""

local_model_dir = "PATH_TO_SAVE"
mistral_models_path = Path(local_model_dir)
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"],
    local_dir=local_model_dir,
    token=access_token
)



tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
model = Transformer.from_folder(mistral_models_path)

model_conclusions = []

system_message = SystemMessage(content=system_message)

for prompt in prompts:
    completion_request = ChatCompletionRequest(messages=[system_message, UserMessage(content=prompt)])

    tokens = tokenizer.encode_chat_completion(completion_request).tokens

    out_tokens, _ = generate([tokens], model, max_tokens=64, temperature=0.0, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
    result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])
    model_conclusions.append(result)



