import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run() -> None:
    async with sse_client("http://localhost:7860/gradio_api/mcp/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 正确取法：访问 .tools
            tools = (await session.list_tools()).tools
            print("可用工具：", [t.name for t in tools])

            result = await session.call_tool(
                "sentiment_analysis",
                arguments={"text": "I hate code!"}
 
            )
            for item in result:
                print("结果：", item)

if __name__ == "__main__":
    asyncio.run(run())