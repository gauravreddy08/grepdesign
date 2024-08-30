from openai import OpenAI
from dotenv import load_dotenv
from src.Repository import Repository
import src.prompt as prompt
import json

load_dotenv(override=True)

class LLM():
    def __init__(self, model_name='gpt-4o', greptile=None):
        self.model = OpenAI()
        self.model_name = model_name

        self.messages = []

        self._append('system', prompt.code_gen)

        if greptile is None:
            raise Exception("Please initialize Graptile first.")
        
        self.greptile = greptile
        self.repository = greptile.repository

        self.git_manager = Repository(self.repository)
        
        f = open('src/tools.json', 'r')
        self.tools = json.load(f)

    def call(self, prompt=None, tool_choice='auto'):

        if prompt: self._append('user', prompt)
        
        completion = self.model.chat.completions.create(
                        model=self.model_name,
                        messages=self.messages,
                        tools = self.tools,
                        tool_choice=tool_choice
                    )
        
        response = completion.choices[0].message.content

        self._append('assistant', str(response))

        tool_calls = completion.choices[0].message.tool_calls
        
        if tool_calls:
            self.messages.append(completion.choices[0].message)
            return self.function_call(tool_calls)
        else:
            return response
    
    def _append(self, role: str, content: str):
        self.messages.append({'role': role,
                              'content': str(content)})
        
    def function_call(self, tool_calls):
        for tool_call in tool_calls:
            if tool_call.function.name == 'write_file':
                function_args = json.loads(tool_call.function.arguments)

                print(f"[INFO] Writing file {function_args.get("filepath")}")

                function_response = self.git_manager.write_file(
                    filepath=function_args.get("filepath"),
                    old_code=function_args.get("old_code"),
                    updated_code=function_args.get("updated_code")
                )
            
            elif tool_call.function.name == 'retriever':
                print(f"[INFO] Accessing Codebase ({self.repository})")
                function_args = json.loads(tool_call.function.arguments)
                query = function_args.get('query')
                query = prompt.greptile_bot.format(user_prompt=query)

                function_response = self.greptile.search(query)

            elif tool_call.function.name == 'push_changes':
                print(f"[INFO] Pushed changes to GitHub ({self.repository})")
                function_response = self.git_manager.push_changes()

            self.messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_call.function.name,
                "content": function_response,
            })
                
        return self.call(tool_choice='auto')

        



