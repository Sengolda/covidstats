"""
The MIT License (MIT)

Copyright (c) 2021-present Sengolda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Any
from dataclasses import dataclass

from datetime import datetime
import requests
import aiohttp



@dataclass
class Stats:
    TotalCases: int
    TotalRecover: int
    TotalCriticalCondition: int
    NewDeathsToday: int


BASE_URL = "https://disease.sh/v3/covid-19/countries"


class CoronaTracker:
    def __init__(self):
        self.current_statics: Stats
        self.total_stats = None

        self._data = {}
        self.__aio_session = None
    


    def fetch_results(self, country):
        r = requests.get(BASE_URL + f"/{country}")

        self._data = r.json()
        self.current_statics = self.sort_stats(self._data)
        return self.current_statics
    

    async def aio_fetch_results(self, country):
        if self.__aio_session is None:
            self.__aio_session = aiohttp.ClientSession()

        r = await self.__aio_session.get(BASE_URL + f"/{country}")

        self._data = await r.json()
        self.countries = self.sort_stats(self._data)
        return self.countries

    
    def sort_stats(self, d):
        return Stats(TotalCases=d['cases'], TotalCriticalCondition=d['critical'],
        TotalRecover=d["active"],
        NewDeathsToday=d["todayCases"]
        )