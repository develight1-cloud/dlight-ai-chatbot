import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the Kimi-K2.5 model and tokenizer
model_name = 'moonshotai/Kimi-K2.5'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Create Gradio interface
iface = gr.Interface(fn=generate_response, inputs="text", outputs="text", title="Kimi-K2.5 Chatbot", description="Ask anything and get a response from Kimi-K2.5 model.")

# Launch the interface
iface.launch()