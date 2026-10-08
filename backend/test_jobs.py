import asyncio

from jobs_service import (
    search_germany_jobs
)


async def main():

    result = await search_germany_jobs(
        keyword="AI Engineer",
        location="Berlin",
        size=5
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())