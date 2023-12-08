from openai import OpenAI
from dotenv import load_dotenv, dotenv_values


class AskGpt:
    client = ""

    def __init__(self):
        try:
            api_key = dotenv_values(dotenv_path="./FTR.env")["GPT_API_KEY"]
            self.client = OpenAI(api_key=api_key)
        except Exception:
            print("There was a problem regarding the OpenAI client")

    def prompt(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt.get("prompt")},
            ]
        )

        print(completion.choices[0].message.content)
        extension = prompt.get("extension", "txt")
        with open(f"./data/filename.{extension}", "w") as f:
            f.write(completion.choices[0].message.content)