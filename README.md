# IoT2021
Internet of Things - Polimi hands-on activities 2021

## Lesson 2 - CoAP

### HTTP 
#### Make a request
- via the browser
- via postman
- via `curl`

#### Make a request via `curl`
##### [HTTP server test](https://github.com/edoardesd/home-HTTPserver)
- install instructions in the repository above
- `sudo python3 server.py`
- normal request: `curl http://0.0.0.0:<port>/living_room/temperature`
- verbose request: `curl -v http://0.0.0.0:<port>/living_room/temperature`

### CoAP
#### Use `Copper`
- start the [CoAP server](https://github.com/edoardesd/home-CoAPServer) 
- open mozilla
- [](coap://localhost:5683/)

##### Restful API
- resource discovery
- `GET`: `coap://127.0.0.1:5683/hello_world`
- `POST`: `coap://127.0.0.1:5683/hello_post`
- `GET`: `coap://localhost:5683/living_room/temperature`
- observe
- `PUT`: `coap://localhost:5683/living_room/door?status=CLOSED`
- `POST`: `coap://localhost:5683/living_room/door?create`

### Wireshark
- filter GET: `coap.code == GET || coap.code == 69`
- filter POST: `coap.code == POST || coap.code == 68`
