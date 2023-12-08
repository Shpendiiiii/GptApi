from openai import OpenAI


class AskGpt:
    client = ""

    def __init__(self):
        self.client = OpenAI(api_key="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")

    def prompt(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                # {"role": "user", "content": "How does powershell get executed, is it compiled?"}
            ]
        )

        print(completion.choices[0].message.content)
