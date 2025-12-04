# /// script
# dependencies = [
#   "mcp",
#   "httpx",
# ]
# ///
import asyncio
import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client

async def run():
    # Try to connect to the SSE endpoint
    url = "http://127.0.0.1:8080/sse"
    print(f"Connecting to {url}...")
    
    try:
        async with sse_client(url) as (read, write):
            print("Connected to SSE endpoint.")
            async with ClientSession(read, write) as session:
                print("Initializing session...")
                await session.initialize()
                
                print("Listing tools...")
                tools = await session.list_tools()
                print(f"Available tools: {[t.name for t in tools.tools]}")
                
                print("Calling get_exchange_rate...")
                result = await session.call_tool(
                    "get_exchange_rate", 
                    arguments={"currency_from": "USD", "currency_to": "EUR"}
                )
                print(f"Result: {result}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run())