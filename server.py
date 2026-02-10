from wsgiref.simple_server import make_server

def application(env, start_response):
  headers = [ ("Content-Type", "text/plain") ]

  start_response("200 OK", headers)

  return [b"Hola mundo, desde mi primer servidor en Python!"]

server = make_server("localhost", 8000, application)
server.serve_forever()