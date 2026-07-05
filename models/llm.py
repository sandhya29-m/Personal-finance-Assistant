# models/llm.py

from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME


class LLMModel:
    """
    Singleton class to initialize the LLM only once.
    """

    _llm = None

    @classmethod
    def get_llm(cls):

        if cls._llm is None:

            cls._llm = ChatGroq(
                api_key=GROQ_API_KEY,
                model=MODEL_NAME,
                temperature=0.3,
                max_tokens=1024,
            )

        return cls._llm


# Global LLM instance
llm = LLMModel.get_llm()