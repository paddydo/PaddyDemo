import gradio as gr
import pandas as pd

def update_table(name, age, team):
    # Create a new row with the input data
    new_row = pd.DataFrame({'Name': [name], 'Age': [age], 'Team': [team]})
    
    # Append the new row to the existing dataframe
    if 'df' not in update_table.__dict__:
        update_table.df = new_row
    else:
        update_table.df = pd.concat([update_table.df, new_row], ignore_index=True)
    
    return update_table.df

# Define Gradio interface
iface = gr.Interface(
    fn=update_table,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Number(label="Age"),
        gr.Textbox(label="Team")
    ],
    outputs=gr.Dataframe(headers=['Name', 'Age', 'Team']),
    title="Team Member Information",
    description="Enter the Name, Age, and Team of a team member. The information will be displayed in the table on the right.",
)

# Launch the app
iface.launch(server_name="0.0.0.0", server_port=7860)