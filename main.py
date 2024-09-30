from openai import OpenAI


client = OpenAI(api_key="sk-SdSDuAtaPQrZ6pCnYsDwPOvjYBykCeyvkuVAE4p89xT3BlbkFJ4AH980PsA5oGDwO8m9ibGrIl7eBpB0gn6kKKqZHOUA")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você:")
        if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
