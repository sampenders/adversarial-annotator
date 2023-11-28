import json

JSON_NAME = "database/adversarial_prompts.json"
def send_to_database(prompt="", expected="", llm_output="", notes=""):
    new_entry = {}
    new_entry['prompt'] = prompt
    new_entry['expected_output'] = expected
    new_entry['llm_output'] = llm_output
    new_entry['notes'] = notes
    with open(JSON_NAME, 'r+') as fp:
        data = json.load(fp)
        data.append(new_entry)
        fp.seek(0)
        json.dump(data, fp, indent=4)


if __name__ == '__main__':
    send_to_database("test", "test3243", "i no not")