TEST_CASES = [

    {
        "name": "Math addition",
        "input": "What is 10 + 20?",
        "expected": "30",
    },

    {
        "name": "Math multiplication",
        "input": "What is 5 * 6?",
        "expected": "30",
    },

    {
        "name": "Task creation",
        "input": "Create a task to practice Python.",
        "expected_contains": "created",
    },

    {
        "name": "Memory",
        "input": "Remember that my favorite language is Python.",
        "expected_contains": "remember",
    },

    {
        "name": "General question",
        "input": "What is Python?",
        "expected_contains": "Python",
    },
    {
    "name": "Coding question",
    "input": "Explain Python functions.",
    "expected_contains": "function",
},

{
    "name": "Research question",
    "input": "Help me research RAG.",
    "expected_contains": "RAG",
},

{
    "name": "Time request",
    "input": "What time is it?",
    "expected_contains": "20",
},

{
    "name": "File request",
    "input": "List my project files.",
    "expected_contains": "main.py",
},

]