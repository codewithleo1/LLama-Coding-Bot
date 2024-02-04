import streamlit as st
from ctransformers import AutoModelForCausalLM
import time

def generate_answer(question, model):
    topic = "Basic Programming"
    language = ""

    prompt = f"""
    <<SYS>>
    you are a teacher answering student's 'question'.
    you should detect code and enclose any coding syntax in '<code> </code>' tag.
    you are only supposed to answer in text that can be spoken, do not use any special characters, bullets, pointers or numbers.
    <</SYS>>
    
    [INST]
    topic: {topic}
    programming language: {language}
    question: {question}
    [/INST]"""

    prompt = model.tokenize(prompt)
    answer = ""
    for token in model.generate(prompt):
        word = model.detokenize(token)
        answer += word
    return answer

def main():
    llm_model = AutoModelForCausalLM.from_pretrained("C:\Users\kavit\Desktop\MasterClass - DS & AI",
                                                      model_file="llama-2-7b-chat.q4_K_M.gguf",
                                                      model_type="llama")

    st.title("Chatbot with Streamlit")

    question = st.text_input("Ask a question:")
    
    if st.button("Generate Answer"):
        start_time = time.time()
        answer = generate_answer(question, llm_model)
        st.write(f"Answer: {answer}")
        st.write("--- %s seconds to generate answer ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
