# Prompt-ly 🛠️

## Overview

Prompt-ly is a powerful tool designed to assist users in creating and refining prompts for various applications, including AI models, creative writing, and brainstorming sessions. This project provides an intuitive interface to generate high-quality prompts tailored to user needs, enhancing creativity and productivity. Powered by Google's Gemini✨

<!-- [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://)) -->

## Features

- **Prompt Generation:** Automatically create prompts based on user-defined themes or topics.
- **Prompt Improvement:** Analyze existing prompts and suggest enhancements to increase clarity, specificity, and engagement.
- **User-Friendly Interface:** Simple and intuitive design for easy navigation and prompt customization.
- **Versatile Applications:** Ideal for writers, educators, marketers, and anyone in need of creative inspiration.

## How to Run on Your Own Machine

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Arsdeep/Prompt-ly.git
   cd Prompt-ly
   ```

2. **Create a Virtual Environment**

   If you are using Python 3, you can create a virtual environment by running:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install the Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the Secrets Configuration**

   Create a directory named `.streamlit` in the root of the project if it doesn't exist:

   ```bash
   mkdir .streamlit
   ```

   Inside the `.streamlit` directory, create a file named `secrets.toml`:

   ```bash
   touch .streamlit/secrets.toml
   ```

   Open `secrets.toml` and add your API keys:

   ```toml
   [general]
   GEMINI_API_KEY = "your_gemini_api_key_here"
   COSTAR_PROMPT = "your_costar_prompt_here"
   ```

   Replace `"your_gemini_api_key_here"` and `"your_costar_prompt_here"` with your actual API key and prompt.

5. **Run the App**

   ```bash
   streamlit run streamlit_app.py
   ```

## License

This project is licensed under the Apache License 2.0

## Contact

If you have any questions or feedback, please open an issue or reach out to me at arsdeepdewangan@gmail.com
