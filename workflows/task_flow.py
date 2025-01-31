from langgraph.graph import StateGraph
from langgraph.prebuilt import ChatAgent
import agents.assistant as assistant
import agents.scheduler as scheduler

workflow = StateGraph()
workflow.add_node("summarization", ChatAgent(assistant.deepseek_assistant))
workflow.add_node("scheduling", ChatAgent(scheduler.scheduler_agent))
workflow.add_edge("summarization", "scheduling")

def run_workflow(task):
    return workflow.run(task)

# Example usage
result = run_workflow("Summarize and schedule: 'Meeting moved to 3 PM tomorrow.'")
print(result)
