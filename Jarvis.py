import wolframalpha
import wikipedia

while True:
    input = input("Question: ")

    try:
        app_id = "8UHTA8-5QGXGEJ4AT"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print (answer)
    except:
        result = wikipedia.summary("India")
        # printing the result
        print(result) 

