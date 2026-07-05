import json
import os


class ConversationMemory:

    FILE_NAME = "memory.json"

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE_NAME):
            return []

        with open(cls.FILE_NAME, "r") as f:
            return json.load(f)

    @classmethod
    def save(cls, history):

        with open(cls.FILE_NAME, "w") as f:
            json.dump(history, f, indent=4)

    @classmethod
    def add_message(cls, role, content):

        history = cls.load()

        history.append({

            "role": role,

            "content": content

        })

        cls.save(history)

    @classmethod
    def clear(cls):

        cls.save([])