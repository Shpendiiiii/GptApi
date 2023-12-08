from api_req import AskGpt
from user_input import give_prompt

while True:
    AskGpt().prompt(give_prompt())
