from smolagents import CodeAgent
from smolagents import DuckDuckGoSearchTool
from smolagents import LiteLLMModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model = LiteLLMModel("ollama/deepseek-coder:1.3b"))


agent.run("用中文告诉我今天北京的天气")