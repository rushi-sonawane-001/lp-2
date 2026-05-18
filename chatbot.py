from nltk.chat.util import Chat,reflections

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1. How are you today? How may I help you?"]
    ],
    [
        r"(.*) name?",
        ["I am a Chatbot. I don't have a particular name"]
    ],
    [
        r"How are you?",
        ["I am fine.","I am always happy to help"]
    ],
    [
        r"I am good",
        ["Nice to hear that"]
    ],
    [
        r"Hi|Hello|Hey|hi|hello",
        ["Hey there","hello"]
    ],
    [
        r"(.*) created?",
        ["I was made by a computer programmer"]
    ],
    [
        r"(.*) investments|money?",
        ["There are many options to invest money like mutual funds, regional banks, etc."]
    ],
    [
        r"(.*) stocks?",
        ["You can invest in companies like Amazon, Tesla, Google, etc."]
    ],
    [
        r"(.*) companies (.*) money?",
        ["Amazon,Tesla"]
    ],
    [
        r"Bye|bye",
        ["Goodbye! Have a nice day"]
    ],
    [
        r"Thanks|thank you",
        ["You are welcome"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that"]
    ]
]

def chat():
    print("Hello I am a chatbot.Type 'quit' to exit")
    obj = Chat(pairs,reflections)
    obj.converse()
chat()

print("Thank you for chatting!")