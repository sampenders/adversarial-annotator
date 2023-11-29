import streamlit as st
import json

def clear_text_area():
    st.session_state["Prompt"] = ""
    # st.session_state["Response"] = ""
    st.session_state["Notes"] = ""
    st.session_state["True_Lables"] = []

# st.markdown(
#     """
#     <style>
#         .title {
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             height: 100vh;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# with st.container() as title_container:
#     st.markdown('<h1 class="title-container">Annotation App</h1>', unsafe_allow_html=True)

st.title("Annotation App")

left_column, right_column = st.columns(2)

prompt = left_column.text_area(label='Prompt', key="Prompt", placeholder="Prompt given to model")
true_label = left_column.multiselect("Choose the true labels you think: ", ["Anger", "Joy", "Optimism", "Pessimism", "Surprise"], key="True_Lables")
notes = left_column.text_area(label='Notes', key="Notes")

response = right_column.text_area(label='Response', key="Response", placeholder="Model's response")


example = {
    'prompt' : prompt,
    'response' : response,
    'notes' : notes,
    'true_label' : true_label
}

with left_column:
    button_col1, button_col2 = st.columns(2)
    save = button_col1.button("Save")
    clear = button_col2.button("Clear", on_click=clear_text_area)

if save:
    # display the balloon to let user know it's submitted
    # st.balloons()

    out_file = 'data.json'
    with open(out_file, 'a') as f:
        # write to the new line of the json file
        f.write(json.dumps(example) + '\n')
        # json.dump(example, f)

    # Display success message
    success_message = st.empty()
    success_message.text("Data saved successfully! Press 'Clear' button for the next input")


