import aiohttp
from bot.config.config import SUBGRAM_MAIN_API, SUBGRAM_SECRET_KEY


class SubgramAPI:
    """
    Асинхронный клиент для взаимодействия с API Subgram.
    :param api_key: API-ключ для аутентификации.
    :param secret_key: Секретный ключ для аутентификации.
    """

    BASE_URL = "https://api.subgram.org"

    _session: aiohttp.ClientSession | None = None
    _connector: aiohttp.TCPConnector | None = None
    _timeout: aiohttp.ClientTimeout | None = None

    def __init__(self, api_key: str = SUBGRAM_MAIN_API, secret_key = SUBGRAM_SECRET_KEY):
        self.api_key = api_key
        self.secret_key = secret_key

    @classmethod
    async def get_session(cls) -> aiohttp.ClientSession:
        if cls._session is None:
            cls._connector = aiohttp.TCPConnector(limit=50)  # макс. 50 соединений одновременно
            cls._timeout = aiohttp.ClientTimeout(total=5)   # таймаут 5 секунд
            cls._session = aiohttp.ClientSession(connector=cls._connector, timeout=cls._timeout)
        return cls._session

    @classmethod
    async def close_session(cls):
        if cls._session:
            await cls._session.close()
            cls._session = None
            cls._connector = None
            cls._timeout = None

    async def create_bot(self, bot_token, get_links: int = 1, max_op: int = 10) -> dict:
        url = f"{self.BASE_URL}/bots"
        payload = {
            "action": "add",
            "bot_token": bot_token,
            "max_op": max_op,
            "get_links": get_links,
            "show_quiz": 0,
            "gender_question": 0
        }
        headers = {
            "Auth": self.secret_key,
            "Content-Type": "application/json"
        }
        session = await SubgramAPI.get_session()
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()

    async def get_tasks(self, api_key: str, user_id: int, chat_id: int, gender: str | None = None,
                        first_name: str | None = None, language_code: str | None = None,
                        premium: bool | None = None, max_op: int = 3,
                        action: str = "subscribe", exclude_channel_ids: list[str] | None = None) -> dict:
        url = f"{self.BASE_URL}/request-op/"
        payload = {
            "UserId": str(user_id),
            "ChatId": str(chat_id),
            "MaxOP": max_op,
            "action": action,
        }
        if gender:
            payload["Gender"] = gender
        if first_name:
            payload["first_name"] = first_name
        if language_code:
            payload["language_code"] = language_code
        if premium is not None:
            payload["Premium"] = premium
        if exclude_channel_ids:
            payload["exclude_channel_ids"] = exclude_channel_ids

        headers = {
            "Auth": api_key,
            "Content-Type": "application/json"
        }
        session = await SubgramAPI.get_session()
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()

    async def check_task(self, api_key: str, user_id: int, links: list[str] | None = None, start_date: str | None = None, end_date: str | None = None) -> dict:
        url = f"{self.BASE_URL}/get-user-subscriptions"
        payload = {
            "user_id": user_id,
            "links": links
        }
        if start_date:
            payload["start-date"] = start_date
        if end_date:
            payload["end-date"] = end_date
        headers = {
            "Auth": api_key,
            "Content-Type": "application/json"
        }
        session = await SubgramAPI.get_session()
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()

    async def get_balance(self) -> dict:
        url = f"{self.BASE_URL}/get-balance"
        headers = {
            "Auth": self.api_key,
            "Content-Type": "application/json"
        }
        session = await SubgramAPI.get_session()
        async with session.post(url, headers=headers) as response:
            return await response.json()

    async def get_statistics(self, api_key: str) -> dict:
        url = f"{self.BASE_URL}/get-statistic/"
        headers = {
            "Auth": api_key,
            "Content-Type": "application/json"
        }
        session = await SubgramAPI.get_session()
        async with session.post(url, headers=headers) as response:
            return await response.json()


subgram_api = SubgramAPI()