import aiohttp
import asyncio
import json

async def fetch_greenhouse():
    url = "https://boards-api.greenhouse.io/v1/boards/airbnb/jobs"
    print(f"Fetching Greenhouse: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                jobs = data.get('jobs', [])
                if jobs:
                    print("Greenhouse Job Keys:", jobs[0].keys())
                    print("Greenhouse Job Sample:", json.dumps(jobs[0], indent=2))
                    # Check if we can get details
                    job_id = jobs[0].get('id')
                    if job_id:
                        detail_url = f"https://boards-api.greenhouse.io/v1/boards/airbnb/jobs/{job_id}"
                        print(f"Fetching Greenhouse Detail: {detail_url}")
                        async with session.get(detail_url) as detail_response:
                            if detail_response.status == 200:
                                detail_data = await detail_response.json()
                                print("Greenhouse Detail Keys:", detail_data.keys())
                                content = detail_data.get('content')
                                print(f"Greenhouse Content Type: {type(content)}")
                                if isinstance(content, str):
                                    print(f"Greenhouse Content Sample: {content[:200]}...")
                else:
                    print("No jobs found for Greenhouse")
            else:
                print(f"Greenhouse Error: {response.status}")

async def fetch_lever():
    url = "https://api.lever.co/v0/postings/palantir"
    print(f"Fetching Lever: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data:
                    print("Lever Job Keys:", data[0].keys())
                    print("Lever Job Sample:", json.dumps(data[0], indent=2))
                else:
                    print("No jobs found for Lever")
            else:
                print(f"Lever Error: {response.status}")

async def main():
    await fetch_greenhouse()
    print("-" * 20)
    await fetch_lever()

if __name__ == "__main__":
    asyncio.run(main())
