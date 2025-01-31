from autogen import AssistantAgent
import config

deepseek_assistant = AssistantAgent(
    name="AI_Assistant",
    system_message="You assist users by summarizing emails, scheduling meetings, and handling queries.",
    llm_config={"model": "deepseek-lm", "api_key": config.DEEPSEEK_API_KEY}
)
