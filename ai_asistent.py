from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")

def chat(sprava):
    odpoved = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Si užitočný asistent v slovenčine."},
            {"role": "user", "content": sprava}
        ]
    )
    return odpoved.choices[0].message.content

print("AI Asistent spustený. Napíš 'koniec' pre ukončenie.\n")

while True:
    vstup = input("Ty: ")
    if vstup.lower() == "koniec":
        print("Dovidenia!")
        break
    print(f"AI: {chat(vstup)}\n")