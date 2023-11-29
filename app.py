import streamlit as st
import json
from utils import send_prompt
from openai import OpenAI
import yaml
import sys
sys.path.append('database')
from feed_database import send_to_database


def clear_text_area():
    st.session_state["Prompt"] = ""
    st.session_state["Notes"] = ""
    st.session_state["True_Labels"] = []

st.title("Adversarial Annotator")

# set up elements
prompt = st.text_area(label='Prompt', key="Prompt", placeholder="Prompt given to model")
true_labels = st.multiselect("Choose ground truth labels: ", ["anger", "joy", "optimism", "pessimism", "surprise"], key="True_Labels")
send_button = st.button('Send to model')
st.divider()
model_response_box = st.empty()
success_status = st.empty()
next = st.button("Next", on_click=clear_text_area)

# send to model
client = OpenAI()
with open('config/model_config.yaml', 'r') as f:
    config = yaml.safe_load(f)
model_params = config['params']
system_instruction = config['system_instruction']

if send_button:
    model_output = send_prompt(system_instruction, prompt, client, model_params)
    # update model output
    model_response_box.text('Model prediction: ' + ', '.join(model_output))
    
    # save prompt if correct
    if set(model_output) != set(true_labels):
        success_status.success('You tricked the model! Click "Next" to try again', icon="✅")
        send_to_database(prompt, true_labels, model_output)
    else:
        success_status.info('You didn\'t trick the model. Click "Next" to try again', icon="❗")