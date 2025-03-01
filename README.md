# Text Summarizer
This is a simple **Text Summarizer** application built using **Streamlit** and the **Hugging Face Transformers** library. The application allows users to generate summaries for text using the **facebook/bart-large-cnn** model.

---

## ✨ Features

- 📄 **Upload a file**: Upload a `.txt` file, and the text will be summarized.
- ✍️ **Enter text directly**: Input text manually in the provided text area for summarization.
- 🔄 **Generate sample text**: Choose from predefined topics (Food, Technology, Health, Education, Politics) to generate sample text for summarization.

---

## 🛠️ Technology Stack

| Component   | Technology               |
|--------------|------------------|
| Framework   | Streamlit               |
| Model         | Facebook BART (bart-large-cnn) |
| Language    | Python                  |
| Library         | Transformers            |

---

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
### Step 2: Set Up Virtual Environment (Recommended)

Setting up a virtual environment keeps your project dependencies isolated and avoids version conflicts.

- **For Windows**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

- **For Linux/macOS**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

---

### Step 3: Install Required Libraries

After activating the virtual environment, install all dependencies using:

```bash
pip install -r requirements.txt

