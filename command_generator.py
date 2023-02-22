# Written by Armaan Kapoor on 12-26-2022
import os
import openai
import argparse

# openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = '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'

def make_request(prompt):
    request = make_openai_request()
    return request.request(prompt)

class make_openai_request:

    def __init__(self):
        self.prompt = ""
        self.temperature = 0.3
        self.frequency_penalty = 0.0
        self.stop = None


    def request(self, prompt):
        self.prompt = prompt
        self.tokensout = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=0.0,
            stop=self.stop,
        )
        return self.tokensout["choices"][0]["text"].strip()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "request" command
parser_request = subparsers.add_parser('request', help='make a request to openai')

# add arguments to the parser
parser_request.add_argument('prompt', help='the prompt to send to openai')


if __name__ == '__main__':
    args = parser.parse_args()
    # to invoke the request command via the command line, run: python main.py request "prompt"
    if args.prompt:
        #read prompt_config.txt 
        with open("prompt_config.txt", "r") as f:
            prompt_config = f.read()
        print(make_request(prompt_config + "\n" + args.prompt + "\n" + "➜"))
    else:
        print("NO PROMPT PROVIDED!")
