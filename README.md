# Practica2-REST

## Introducción
Programa muy simple en el cual mediante un script en bash simulamos 3 clientes que envían 3 números aleatorios a un servidor. Una vez éste los recibe decide si hay consenso o no. Para que haya consenso almenos dos de ellos tienen que ser iguales

```mermaid
sequenceDiagram
participant Server
loop Every 10 seconds
Client 1->> Server:Random number
Client 2->> Server:Random number
Client 3->> Server:Random number
Note right of Server: Check if there <br/> is consensus
end
```
  

## Instrucciones

### Ejectuar el servidor 
```console
export FLASK_APP=app.py  
python3 -m flask run
```

### Dar permisos al script del cliente
```console
chdmod +x script.sh
```
### Ejecturar el script del cliente
```console
./script.sh
```