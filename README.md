# trabalho_4

Esse trabalho visa calcular fibonacci ou fatorial a depende do que voce queira
Para isso é necessário que voce rode o código e vá no seu terminal e digite:
 Invoke-WebRequest -Uri http://127.0.0.1:5000/api/calculos -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"operacao": "fatorial/fibonacci", "numero": x}' -UseBasicParsing
Caso voce esteja usando Windows, ou 
curl -X POST -H "Content-Type: application/json" -d '{"operacao": "fatorial/fibonacci", "numero": x}' http://127.0.0.1:5000/api/calculos
Caso voce esteja usando linux
em que x é o termo de fibonacci ou o fatorial que voce quer que ele printe
e fatorial/fibonacci voce deve selecioanr um que voce queira
