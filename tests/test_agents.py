import unittest
from agents.assistant import deepseek_assistant

class TestAIResponses(unittest.TestCase):
    def test_email_summarization(self):
        email_text = "Meeting is moved to 3 PM tomorrow."
        response = deepseek_assistant.generate(f"Summarize: {email_text}")
        self.assertIn("3 PM", response)

if __name__ == "__main__":
    unittest.main()
