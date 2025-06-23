# 🧠 AI Coding Agent — Python Calculator Project

This project is a learning-oriented **AI coding agent** capable of understanding tasks, analyzing code, running Python files, and modifying project files using the **Gemini API** (by Google).  
The agent can reason through multi-step instructions and invoke functions automatically based on context.

---

## 📁 Project Structure
```
project/
├── calculator/
│   ├── main.py              # Entry point for the calculator
│   └── pkg/
│       ├── calculator.py    # Core expression evaluation logic
│       └── render.py        # Result formatting as a text box
├── functions/
│   ├── call_function.py     # Central function-call dispatcher
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── main.py                  # Main CLI interface for the agent
├── .env                     # Stores Gemini API key
└── README.md                # Project documentation
```


## 🚀 Getting Started

### 1. Set up the environment

Create a `.env` file in the root directory and add your **Gemini API key**:

```env
GEMINI_API_KEY=your-api-key-here
```
### 2. Install dependencies
Make sure you have Python 3.9+ installed, then run:
```
pip install -r requirements.txt
```

### 3. Run the agent
You can now start chatting with the AI agent from your terminal:
```
python main.py "how does the calculator render results to the console?" --verbose
```
Use --verbose to see detailed function calls and step-by-step processing.