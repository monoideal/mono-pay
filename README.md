web3 payment gateway; built with Django 4

## flow:

1. create a payment gateway (w/ script) and get gateway slug (BASE_URL/payments/pay/gateway_slug)
2. user sends payment to randomly generated wallet
3. validate balance: a) received expected amount; b) received more than expected amount (refund diff); c) received less than expected (bounce refund to sender)
4. tx fee will be paid by gateway operator; refund tx fee will be paid by sender
5. signed receipt or error status shown to user; redirect to callback
6. status can be queried at .../gateway_slug

## License
[MIT](https://choosealicense.com/licenses/mit/)
