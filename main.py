import google.generativeai as genai
API_KEY="AIzaSyCyZovyiPD4Mjif1Gzkv6dori7OAudau1s"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-pro')
while True:
  print("Gemini: ", end="")
  query=input("what do you want to know today?\n Your response: ")
  if query == "exit":
    print("Gemini: \n Bye!")
    break
  response=model.generate_content(query)
  print("Gemini: ", end="")
  print(response.text)