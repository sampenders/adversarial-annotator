import streamlit as st
import json

st.title('Annotation App')

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
true_label = left_column.radio("True label", ["Positive", "Negative"])

prompt = right_column.text_area(label='Prompt', placeholder="Prompt given to model")
response = right_column.text_area(label='Response', placeholder="Model's response")
notes = right_column.text_area(label='Notes')

example = {
    'prompt' : prompt,
    'response' : response,
    'notes' : notes,
    'true_label' : true_label
}

save = right_column.button("Save")
if save:
    out_file = 'data.json'
    with open(out_file, 'w') as f:
        json.dump(example, f)
