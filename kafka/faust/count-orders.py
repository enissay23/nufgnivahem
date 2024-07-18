import faust

class Order(faust.record):
    product: str
    quantity: int

app = faust.App('count-orders', broker='kafka://localhost:9092')
topic = app.topic('topic1', value_type=Order)

@app.agent(topic)
async def count(orders):
    async for order in orders:
        print(f'product: {order.product}, quantity: {order.quantity}')


if __name__ == '__main__':
    app.main()