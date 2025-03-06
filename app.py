import os
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_WATCHDOG"] = "false"
os.environ["STREAMLIT_WATCHFILES_IGNORE"] = "torch"
os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = '1'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

import streamlit as st
from transformers import pipeline

# Set up the text summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Set page title
st.title("Text Summarizer")

# Choose input method
input_method = st.radio(
    "Choose input method:",
    ["Upload a file", "Enter text directly", "Generate sample text"]
)

# Function to read file
def read_file(uploaded_file):
    try:
        return uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return ""

# Initialize the input_text variable to avoid the NameError
input_text = ""

# Display appropriate input method
if input_method == "Upload a file":
    uploaded_file = st.file_uploader("Upload your file", type=["txt"])
    if uploaded_file:
        input_text = read_file(uploaded_file)

elif input_method == "Enter text directly":
    input_text = st.text_area("Enter text here:")

elif input_method == "Generate sample text":
    topic = st.selectbox("Select a topic", ["Food", "Technology", "Health", "Education", "Politics"])
    sample_texts = {
        "Food": (
            "Pizza is one of the most popular dishes in the world. It is made with dough, cheese, and various toppings. "
            "The variations in pizza styles, including Neapolitan, New York-style, and Chicago deep-dish, offer endless "
            "flavors. Pizza also represents the cultural and historical significance of food evolution. "
            "Pizza has been enjoyed for centuries, originating from ancient cultures that prepared flatbreads with toppings. "
            "The modern pizza we recognize today evolved in Italy, with the introduction of tomatoes from the Americas. "
            "The combination of cheese, meats, vegetables, and a flavorful sauce on a crispy crust makes it a versatile meal."
            "From its roots in Naples to global chains, pizza is now enjoyed worldwide, each country adding its own unique twist. "
            "Variations like vegan pizza, gluten-free crusts, and the rise of creative toppings, like pineapple or seafood, have sparked debates. "
            "No matter how it's made, pizza continues to bring people together, whether it's shared during family dinners, parties, or casual gatherings. "
            "Pizza is more than just food; it's an experience that transcends borders and unites people of different cultures. "
            "The diversity in pizza types, such as wood-fired, brick oven, and pan pizzas, reflects a growing appreciation for culinary craftsmanship. "
            "In many cultures, pizza is not just a meal, but a form of art, with each region creating its own interpretation. "
            "For example, Italian pizza is known for its simplicity, while American pizza often features a thicker crust and a variety of toppings. "
            "Pizza is also evolving, with more plant-based alternatives and innovative ingredients catering to different dietary preferences. "
            "The popularity of pizza has inspired festivals, competitions, and even pizza-making schools around the world, highlighting its global appeal. "
            "Every year, new pizza trends emerge, from fusion pizzas incorporating different cuisines to the use of organic and locally sourced ingredients. "
            "The universal love for pizza is reflected in its ability to adapt to changing tastes, preferences, and cooking techniques. "
            "From humble beginnings to becoming a symbol of comfort and celebration, pizza continues to evolve, embracing both tradition and innovation."
        ),
        "Technology": (
            "Technology has reshaped human interaction, transforming communication and work through smartphones and the internet. "
            "Artificial Intelligence and machine learning are making significant strides in areas like healthcare, education, "
            "and robotics. The future of technology is full of opportunities and challenges in sustainability and ethics. "
            "From the rise of the internet to cloud computing, technology has continually advanced in ways that have revolutionized industries. "
            "We now live in an era where smart devices and the Internet of Things (IoT) are interconnected, creating efficiencies and convenience. "
            "AI-powered technologies are transforming the workforce, with automation and data analytics paving the way for new innovations. "
            "In healthcare, breakthroughs such as precision medicine and telemedicine are enhancing patient care and access. "
            "Education has become more accessible with online platforms, virtual classrooms, and AI-assisted learning tools. "
            "However, with rapid technological growth come significant challenges. Issues such as cybersecurity, data privacy, and the digital divide must be addressed. "
            "The ethical implications of emerging technologies, such as facial recognition and autonomous machines, are also major concerns. "
            "Tech companies are investing heavily in research and development to create the next generation of digital tools and platforms. "
            "One of the most promising areas is quantum computing, which holds the potential to solve complex problems far beyond the reach of today's computers. "
            "Blockchain technology, best known for its association with cryptocurrencies, is being explored for applications in secure transactions and supply chain management. "
            "Social media platforms continue to evolve, becoming powerful tools for marketing, networking, and even political activism. "
            "The development of 5G networks is set to enhance internet connectivity and speed, enabling more immersive experiences in areas like virtual reality and autonomous vehicles. "
            "Technology is also playing a critical role in addressing environmental issues, from clean energy solutions to innovations in waste management. "
            "The rapid pace of technological advancement calls for a thoughtful approach to policy-making, ensuring that innovations serve the public good while mitigating potential harms. "
            "As technology continues to advance, it will be essential to strike a balance between progress and ethical responsibility."
        ),
        "Health": (
            "Good health is essential for a fulfilling life. Regular exercise, balanced nutrition, and mental well-being are key components. "
            "Advancements in healthcare technology, such as telemedicine and precision medicine, have improved accessibility and treatment outcomes. "
            "Chronic conditions like diabetes, heart disease, and obesity are growing global concerns, but preventive measures and lifestyle changes can help combat these issues. "
            "Mental health is equally important as physical health, with increased awareness of conditions like depression, anxiety, and stress. "
            "Access to quality healthcare varies globally, but initiatives in public health and medical research continue to improve standards. "
            "Innovations in medicine, such as gene editing and stem cell research, hold promise for curing previously untreatable diseases. "
            "The ongoing pandemic has highlighted the importance of public health systems, emphasizing the need for global cooperation in combating infectious diseases. "
            "Mental health care is being increasingly recognized as an integral part of healthcare systems, with a growing focus on therapy, counseling, and support networks. "
            "The healthcare industry is also undergoing a digital transformation, with health apps, wearable devices, and remote monitoring systems becoming more prevalent. "
            "Preventive care is gaining traction, with a focus on early detection and lifestyle changes to reduce the burden of disease. "
            "Vaccination programs have played a critical role in controlling infectious diseases, and new vaccines continue to be developed for emerging threats. "
            "Public health campaigns are raising awareness about the importance of mental health, nutrition, and exercise in promoting overall well-being. "
            "The convergence of healthcare and technology is opening up new possibilities for patient care, from AI-driven diagnostics to personalized treatment plans. "
            "As healthcare systems around the world evolve, the goal is to ensure that all individuals have access to the care they need for a long and healthy life."
        ),
        "Education": (
            "Education fosters intellectual and social development, paving the way for innovation and societal progress. "
            "Modern education systems leverage technology to enhance learning experiences and reach a broader audience. "
            "E-learning platforms, online courses, and digital classrooms are breaking down geographical and financial barriers to education. "
            "In many parts of the world, access to education is still limited, but efforts to improve literacy and provide educational resources are gaining momentum. "
            "Curriculum changes and a focus on critical thinking, creativity, and problem-solving skills are reshaping the learning experience. "
            "From early childhood education to higher education, the value of lifelong learning is being emphasized, with a shift toward skills development and continuous professional growth. "
            "Education is not just about textbooks; it is about equipping individuals with the tools to navigate the complexities of the modern world. "
            "With the increasing adoption of digital technologies, educators are exploring new ways to engage students and provide personalized learning experiences. "
            "Gamification, virtual simulations, and adaptive learning systems are becoming integral parts of modern education, enhancing student engagement and achievement. "
            "Global initiatives are pushing for more inclusive education, ensuring that all children, regardless of their background, have the opportunity to learn. "
            "The development of open educational resources and MOOCs (Massive Open Online Courses) has made education more accessible to individuals around the world. "
            "Higher education institutions are evolving, offering more flexible learning options, such as online degrees, hybrid courses, and micro-credentials. "
            "Education is not only about acquiring knowledge but also about developing skills that are relevant to the needs of the workforce. "
            "Collaborations between educational institutions, industries, and governments are essential for creating relevant curricula that meet the demands of the job market."
        ),
        "Politics": (
            "Politics plays a critical role in decision-making and governance. From democratic systems to authoritarian regimes, "
            "political structures shape economic policies, international relations, and societal norms. Active citizen participation "
            "is crucial for effective governance. Political ideologies influence the direction of public policy, shaping issues such as healthcare, education, and economic equality. "
            "In democracies, elections are held to ensure that the government is accountable to the people, whereas in authoritarian states, political power is concentrated in the hands of a few. "
            "Global politics has become increasingly interconnected, with international organizations like the United Nations and treaties such as the Paris Agreement aiming to address global issues like climate change and human rights. "
            "Political polarization has risen in many countries, with differing opinions on topics such as immigration, taxation, and social justice. "
            "Understanding the political landscape is essential for citizens to make informed decisions and contribute to the betterment of society. "
            "Political discourse has been deeply influenced by social media, with platforms enabling the rapid spread of ideas, movements, and information. "
            "National politics is shaped by global events, with issues like trade, war, and international diplomacy affecting domestic policies. "
            "Human rights and social justice movements continue to push for reforms, challenging systemic inequality and advocating for equality across all sectors of society."
        )
    }
    input_text = sample_texts.get(topic, "")

# Summary options with extended range
max_length = st.slider("Enter maximum summary length:", min_value=150, max_value=800, value=200)
min_length = st.slider("Enter minimum summary length:", min_value=100, max_value=800, value=150)
use_bullet_points = st.checkbox("Use bullet points in summary")

# Show the input text
if input_text:
    st.subheader("Input Text:")
    st.write(input_text)

# Button to generate summary
if st.button("Generate Summary"):
    if not input_text.strip():
        st.error("Please provide text to summarize.")
    else:
        try:
            summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
            if use_bullet_points:
                summary = summary.replace(". ", ".\n- ")
                summary = "- " + summary

            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error generating summary: {e}")
