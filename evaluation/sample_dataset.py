evaluation_dataset = [

    # ===============================
    # Python.pdf
    # ===============================

    {
        "question": "What is Python?",
        "ground_truth": "Python is a high-level, interpreted programming language."
    },

    {
        "question": "What are the features of Python?",
        "ground_truth": "Python is simple, easy to learn, interpreted, object-oriented, portable and supports a large standard library."
    },


    {
        "question": "What programming paradigms does Python support?",
        "ground_truth": "Python supports procedural, object-oriented, and functional programming paradigms."
    },

    {
        "question": "Where is Python commonly used?",
        "ground_truth": "Python is widely used in web development, data analysis, artificial intelligence, machine learning, scientific computing, and automation."
    },

    {
        "question": "Why is Python easy to learn and use?",
        "ground_truth": "Python emphasizes simplicity and readability and uses plain English-like words, making it easy to understand."
    },

    {
        "question": "What does the print() function do in Python?",
        "ground_truth": "The print() function displays text on the screen."
    },

    {
"question": "In which range of themes do the funds engage across?",
"ground_truth": "The funds engage across a wide range of themes, including defence of the territories, adaptation, sustainable livelihoods, biodiversity, forests and agroecology, food security, climate adaptation, and emergency response."
},
{
"question": "What opportunity do Global South funds for socioenvironmental justice offer?",
"ground_truth": "Global South funds for socioenvironmental justice offer an opportunity to drive effective change through bottom-up solutions that take advantage of the knowledge, resources and capacities of communities."
},

    # ===============================
    # Intentional unsupported question
    # ===============================
]
unsupported_questions = [
 
    {
        "question": "What is the time complexity of Python's dictionary lookup?",
        "expected": "Not enough information in the uploaded documents."
    }

]