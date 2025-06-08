import gradio as gr
from gemini_api import generate_project_ideas

def process_input(skills, domain):
    """
    Process user input and generate project ideas.
    
    Args:
        skills (str): User's skills/technologies
        domain (str): Selected domain
    
    Returns:
        str: Generated project ideas
    """
    if not skills.strip():
        return "Please enter your skills/technologies."
    
    return generate_project_ideas(skills, domain)

# Create the Gradio interface
with gr.Blocks(title="Tech2Idea Generator", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🚀 Tech2Idea Generator
    Transform your technical skills into unique project ideas!
    
    Enter your skills/technologies (comma-separated) and optionally select a domain.
    """)
    
    with gr.Row():
        with gr.Column():
            skills_input = gr.Textbox(
                label="Your Skills/Technologies",
                placeholder="e.g., Python, HTML, Flask, Machine Learning",
                lines=3
            )
            domain_dropdown = gr.Dropdown(
                label="Domain (Optional)",
                choices=["Web Development", "AI/ML", "Game Development", "Automation", "Mobile Development", "Data Science"],
                value=None
            )
            generate_btn = gr.Button("Generate Ideas", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(
                label="Generated Project Ideas",
                lines=15,
                show_copy_button=True
            )
    
    generate_btn.click(
        fn=process_input,
        inputs=[skills_input, domain_dropdown],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch() 
