import asyncio
import aiohttp


async def create_link(all_data: list[dict]):
    links = list(map(lambda data: f"https://apietender.uzex.uz/api/common/GetTrade/{data.get('lot_id')}/0", all_data))
    return links


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main(all_data):
    url_list = []
    if isinstance(all_data, list):
        url_list = await create_link(all_data)
    elif isinstance(all_data, int):
        url_list = [f"https://apietender.uzex.uz/api/common/GetTrade/{all_data}/0"]
    async with aiohttp.ClientSession() as session:
        responses = [asyncio.ensure_future(fetch(session, url)) for url in url_list]
        resp_json = await asyncio.gather(*responses)
        return resp_json


async def fetch_new_data(all_data):
    return await main(all_data)


async def fetch_deal(session, url, data):
    async with session.post(url=url, json=data) as response:
        return await response.json()


async def get_deal_cost(pk):
    from_ = 1
    to_ = 50
    url = "https://apietender.uzex.uz/api/common/DealsList"
    while True:
        if to_ >= 1000:
            return ''
        async with aiohttp.ClientSession() as session:
            responses = await fetch_deal(session, url, data={
                "From": from_,
                "To": to_,
                "currencyId": None,
                "System_Id": 0
            })
            deal_cost = list(filter(lambda x: x.get('trade_id') == pk, responses))
            if deal_cost:
                return deal_cost[0].get('deal_cost')
            from_ = to_
            to_ += 50
