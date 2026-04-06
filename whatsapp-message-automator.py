import os
from groq import Groq
client = Groq(api_key="YOUR_API_KEY")

def generate_meassage():
    message_type = input("Type absent/examinations/fees: ").lower().strip()
    student_name = input("Enter student name: ")
    class_name = input("Enter class name: ")
    contact_number = input("Enter the contact number for the institute: ")
    if message_type == "absent":
        prompt = (f"Generate a WhatsApp message from a coaching institute to a parent informing them about their  child {student_name} studying in class {class_name}, Include the institute contact number {contact_number} at the end of each message. Situation: absent . Keep it short and to the point no fluff and generate it in 3 languages Hindi, Marathi and English ")
    elif message_type == "examinations":
        prompt = (f"Generate a WhatsApp message from a coaching institute to a parent informing them about their  child {student_name} studying in class {class_name}, Include the institute contact number {contact_number} at the end of each message. Situation: Examinations . Keep it short and to the point no fluff and generate it in 3 languages Hindi, Marathi and English ")
    elif message_type == "fees":
        prompt = (f"Generate a WhatsApp message from a coaching institute to a parent informing them about their  child {student_name} studying in class {class_name}, Include the institute contact number {contact_number} at the end of each message. Situation: Fees unpaid . Keep it short and to the point no fluff and generate it in 3 languages Hindi, Marathi and English ")
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile" ,
        messages=[
            {"role": "system", "content": "You are a professional manager for a coaching institute in India your role is to create messages in 3 languages with precision and perfection no fluff"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content
result = generate_meassage()
print(result)
