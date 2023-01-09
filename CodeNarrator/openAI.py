import openai
import os
api_key = os.environ["OPENAI_API_KEY"]

openai.api_key = api_key
model_engine = "text-davinci-002"

prompt = "What is the meaning of life?"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
