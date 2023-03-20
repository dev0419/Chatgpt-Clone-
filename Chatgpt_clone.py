import gradio as gr
import openai

openai.api_key = "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"

message_history = [{"role": "user", "content": f"You are a health assistant bot. I will specify the subject matter in my messages, and you will advice with a  that includes the subjects I mention in my messages. Reply only with relevant information to further input. If you understand, say OK."},
                   {"role": "assistant", "content": f"OK"}]

def predict(input):
    
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=message_history
    )
    
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    
    
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]  
    return response


with gr.Blocks() as demo: 

    
    chatbot = gr.Chatbot() 

    
    with gr.Row(): 
        
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
    
    txt.submit(predict, txt, chatbot)

    
    txt.submit(None, None, txt, _js="() => {''}") 
         
demo.launch(share = True)
