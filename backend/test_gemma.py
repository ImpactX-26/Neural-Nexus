import asyncio
from gemma_service import ask_gemma


async def main():

    response = await ask_gemma(
        "Explain artificial intelligence in 3 simple sentences."
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())