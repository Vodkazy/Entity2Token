## A Tool for Entity Recognition

## Fuction1 : Replace entity with <Entity> token

### File

Main.py

### Usage

run this command

```python
    python Main.py
```

and this service will be running at localhost:4399.
If you wanna have a query,please use curl in dos window,and send this message to server.

```python
    curl -XPOST 'localhost:4399/dbpediaEntity2Token' -H 'Content-Type: application/json' -d"{\"question\":\"Norway has a lot of electric cars-so many that it can make anyone driving a new vehicle with an internal combustion engine look like a Luddite. \"}"
```
If you want someone else to call your service, please change `localhost` to your `ip`.


## Fuction2 : Get NER infomation

### Usage

Same as the usage mentioned in *Fuction1*, just need to replace `dbpediaEntity2Token` with `getNER`.

### Note

If there are some Non-ASCII character in your question, please encode them into utf-8 and then send the request, otherwise the server will occur some problems (because of the bug of 'request' function) and can't return the correct answer for you.