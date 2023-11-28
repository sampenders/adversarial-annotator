from openai import OpenAI
import yaml
import re

def send_prompt(instruction, user_text, client, model_params):
    '''
    instruction: instruction dict for system
    user_text: the adversarial prompt
    client: OpenAI object
    model_params: Dict of params to give chat completion 
    '''
    message = instruction
    user_dict = {"role" : "user", "content" : user_text}
    message.append(user_dict)
    output = client.chat.completions.create(
        **model_params, result
        messages=message
    )
    results = output.choices[0].message.content
    results = results.lower()
    results = re.sub('\n', '', results)
    results = re.split('\s*,\s*', results)
    return results

if __name__ == "__main__":
    client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
    ) 

    with open('config/model_config.yaml', 'r') as f:
        openai_config = yaml.safe_load(f)
    instruction = openai_config['system_instruction']
    model_params = openai_config['params']

    input = "I can't believe how good everything has been going!"
    result = send_prompt(
        instruction=instruction,
        user_text=input,
        client=client,
        model_params=model_params
    )
    print(result)
