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

---

## 🔧 Setup & Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ashritha-Satya/TextSummarizer.git
    cd TextSummarizer
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

---

## 📜 Usage

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Enter or paste text into the input box OR upload a `.txt` file.
3. Click the "Summarize" button.
4. View the generated summary along with word count comparison.

---

## 📦 Example Output

**Original Text:**  
*"Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems."*

**Summary:**  
*"AI simulates human intelligence using machines."*

---

## 🏅 Future Enhancements

- Allow users to select different summarization models (like T5, BART).
- Support for multiple file formats (PDF, DOCX).
- Add multilingual summarization support.
- Save and download summary feature.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or want to improve the project, feel free to fork this repository and raise a pull request.

---

## 📧 Contact

**Developer:** Penke Ashritha Satyasri  
**GitHub:** [Ashritha-Satya](https://github.com/Ashritha-Satya)  
**LinkedIn:** [Ashritha Penke](https://www.linkedin.com/in/ashritha-penke-385560259)  
**Email:** ashrithapenke124@gmail.com

---

## ⚖️ License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute this project as per the license terms.

---

⭐ **If you like this project, please star the repository!** ⭐
