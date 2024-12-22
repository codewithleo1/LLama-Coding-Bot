# LLama-Coding-Bot

## Overview
The LLama-Coding-Bot is a Streamlit-based chatbot designed to assist users in learning and solving programming-related questions. It leverages the Llama 2 7B Chat model to generate answers in a conversational format. The bot is programmed to identify and format code snippets and provide explanations suitable for spoken communication.

## Features
- **Interactive Chat Interface:** Built with Streamlit for an intuitive user experience.
- **LLM-Powered Responses:** Uses the Llama 2 7B Chat model for generating contextually accurate answers.
- **Code Syntax Detection:** Automatically wraps code snippets within `<code>` tags for clarity.
- **Custom Prompting:** Tailored prompts to simulate a teacher-student interaction.

## Prerequisites
- Python 3.8 or higher.
- A local installation of the Llama 2 7B Chat GGUF model.
- Required Python libraries: `streamlit`, `ctransformers`, and `time`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd LLama-Coding-Bot
   ```

2. Install dependencies:
   ```bash
   pip install streamlit ctransformers
   ```

3. Download the Llama 2 7B Chat GGUF model:
   - Visit [TheBloke/Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF).
   - Download the `llama-2-7b-chat.q4_K_M.gguf` file.
   - Place the file in a directory (e.g., `C:\Users\kavit\Desktop\MasterClass - DS & AI`).

## File Structure
```
LLama-Coding-Bot/
├── chat_main.py     # Core chatbot logic
├── chat_app.py      # Entry point for the application
├── README.md        # Documentation (this file)
```

## Usage

1. Run the chatbot application:
   ```bash
   streamlit run chat_app.py
   ```

2. Open the chatbot interface in your web browser (typically `http://localhost:8501`).

3. Type your question in the input box and press **Generate Answer**.

## Code Explanation
### chat_main.py
- **`generate_answer(question, model)`**:
  - Prepares a prompt including the topic and programming language.
  - Uses the Llama model to generate a conversational response.

- **`main()`**:
  - Initializes the Llama 2 7B Chat model.
  - Creates a Streamlit interface for users to input their questions and view answers.

### chat_app.py
- Serves as an entry point that calls the `main()` function from `chat_main.py`.

## Notes
- Ensure the model path and file name are correctly set in `chat_main.py`.
- The bot is optimized for text-based questions. Future improvements can include support for advanced topics and dynamic language detection.

## Contributing
Feel free to open issues or submit pull requests to improve the bot.

## License
This project is open-source and available under the MIT License.

---
Happy Coding!
