import os
import openai
import json


class QuestionRequest:
    def ask_question(self, question_prompt):
        start_sequence = "\nA:"
        restart_sequence = "\n\nQ:"
        openai.api_key = "placeholder"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question_prompt,
            temperature=0.8,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\\n"],
        )
        json_string = json.dumps(response)
        json_response = json.loads(json_string)
        print(json_response["choices"][0]["text"])
        return json_response["choices"][0]["text"]


q = QuestionRequest()
q.ask_question("Which numbers comes after 24?")
