
import asyncio
#dispatcher in python 
class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def add_handler(self, event, handler):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(handler)

    def dispatch_event(self, event, *args, **kwargs):
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler(*args, **kwargs)


class Button:
    def __init__(self, name):
        self.name = name
        self.dispatcher = EventDispatcher()

    async def click_async(self):
        print(f"Button {self.name} clicked asynchronously.")
        await asyncio.sleep(1)  # Simulate asynchronous task
        self.dispatcher.dispatch_event('click')

    def click_sync(self):
        print(f"Button {self.name} clicked synchronously.")
        self.dispatcher.dispatch_event('click')


def handle_button_a_click():
    print("Handling click event for Button A")


def handle_button_b_click():
    print("Handling click event for Button B")


# Create buttons
button_a = Button("A")
button_b = Button("B")

# Register event handlers
button_a.dispatcher.add_handler('click', handle_button_a_click)
button_b.dispatcher.add_handler('click', handle_button_b_click)

# Synchronous button clicks
button_a.click_sync()
button_b.click_sync()

# Asynchronous button clicks
async def async_button_clicks():
    await asyncio.gather(
        button_a.click_async(),
        button_b.click_async()
    )

asyncio.run(async_button_clicks())

