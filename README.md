# Weebhooks
A simple Webhooks client for [Discord](https://discordapp.com)

## Install
```sh
pip install weebhooks
```

## Usage
```py
from weebhooks import Weebhook, Embed

hook = Weebhook("WebhookURL", is_async=False)
hook.send("Hello World!")
em = Embed(title="Hello", color=0xff0000).add_field("name", "value")
hook.send(embed=em)
```

## Async
```py
import asyncio
from weebhooks import Weebhook

async def main():
    hook = Webhook("URL", is_async=True)
    await hook.send("Hello, Async!")

asyncio.get_event_loop().run_until_complete(main())
```

## License
[MIT](LICENSE)
