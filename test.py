from server import Client
client = Client()
print(client.set('k1', 'v1'))
print(client.get('k1'))

client.mset('k1', 'v1', 'k2', ['v2-0', 1, 'v2-2'], 'k3', 'v3')