# LangGraph_chatbot


ReAct:
- Act: The model calls specific tools
- Observe: Passes the tools output back to the model
- Reason: Based on the output Repsonse from the tool and input, the model will decide what to do in the next steps.

# ReAct Architecture
<img width="222" height="260" alt="Screenshot 2025-07-18 at 9 10 34 AM" src="https://github.com/user-attachments/assets/61a1253d-eae4-4bc4-b1b1-55fdc582ac8f" />


# ArXiv tool call:
Provided ArXiv number in the Chatbot
<img width="1001" height="545" alt="Screenshot 2025-07-18 at 9 11 04 AM" src="https://github.com/user-attachments/assets/5741ef07-37f5-4040-bb2b-80fc7926fee0" />


# Web Search
Searches through website for the latest data/news
<img width="1001" height="552" alt="Screenshot 2025-07-18 at 9 37 20 AM" src="https://github.com/user-attachments/assets/f258023d-82a2-4346-b781-6456354b8548" />


# Multiple Questions are answred:
If you see the architecture, the tool once get the answer it gets back to LLm again.

<img width="1001" height="545" alt="Screenshot 2025-07-18 at 9 11 48 AM" src="https://github.com/user-attachments/assets/9ecd574b-4910-47a5-85c9-72bba2d7b26b" />


# Memory:
I have asked the question, and in next chat also I wanted to know if it remembers the first question:
<img width="1001" height="417" alt="Screenshot 2025-07-18 at 9 12 31 AM" src="https://github.com/user-attachments/assets/a10c11d9-ad34-47b4-8f2f-e52d115e51dd" />
