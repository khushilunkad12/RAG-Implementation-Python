evaluation_dataset = [

    # ===============================
    # Supported questions
    # ===============================

    {
        "question": "What is Python?",
        "ground_truth": "Python is a high-level, interpreted programming language designed with an emphasis on readability and developer productivity."
    },

    {
        "question": "What programming styles does Python support?",
        "ground_truth": "Python supports procedural, object-oriented, and functional programming styles."
    },

    {
        "question": "What built-in data structures does Python provide?",
        "ground_truth": "Python provides built-in data structures such as lists, tuples, dictionaries, and sets."
    },

    {
        "question": "What are common uses of Python?",
        "ground_truth": "Python is widely used in web development, data analysis, scientific computing, automation, scripting, and artificial intelligence."
    },

    {
        "question": "Which frameworks can be used to build web applications with Python?",
        "ground_truth": "Django and Flask can be used to build server-side applications and APIs."
    },

    {
        "question": "Why are virtual environments used in Python projects?",
        "ground_truth": "Virtual environments are commonly used to keep project dependencies isolated."
    },

    {
        "question": "How can developers improve Python code quality?",
        "ground_truth": "Code quality improves when functions have clear responsibilities, variables have meaningful names, repeated logic is avoided, and formatting and linting tools are used."
    },

    {
        "question": "What are some limitations of Python?",
        "ground_truth": "Python prioritizes developer productivity rather than maximum execution speed. For CPU-intensive workloads, developers may use optimized libraries, parallel processing, compiled extensions, or another language."
    },


    # ===============================
    # Unsupported questions
    # ===============================

    {
        "question": "What is the time complexity of Python dictionary lookup?",
        "ground_truth": "Not enough information in the uploaded documents."
    },

    {
        "question": "Who created Python?",
        "ground_truth": "Not enough information in the uploaded documents."
    },


    # ===============================
    # Follow-up questions
    # ===============================

    {
        "question": "Where is Python commonly used?",
        "ground_truth": "Python is widely used in web development, data analysis, scientific computing, automation, scripting, and artificial intelligence."
    },

    {
        "question": "What can developers use for testing Python applications?",
        "ground_truth": "Automated testing can be added using frameworks such as pytest or the standard unittest module."
    }
]