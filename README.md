# CovidStats
> A Covid Statics tracker.

## Install
```sh
pip install -U git+https://github.com/Sengolda/covidstats
```

## Quick Example
```py
from covidstats import CoronaTracker

my_traker = CoronaTracker()
my_traker.fetch_results("Mexico")
print(my_traker.current_statics)
```

## Quick Example (Async/Await)
```py
from covidstats import CoronaTracker
import asyncio

async def main():
  my_traker = CoronaTracker()
  await my_traker.aio_fetch_results("Mexico")
  print(my_traker.current_statics)

asyncio.run(main())
```

