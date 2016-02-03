Cabe destacar que:

* Una vez levantado el servidor, especificando la ip (a menos que sea localhost, para lo cual ya esta configurado) y el puerto
(que tiene uno por defecto, pero se puede cambiar en la tercer o cuarta linea del archivo), se pueden conectar la cantidad
de clientes que uno especifique en el servidor mismo, en la linea de:

#servidor.listen(X)

* En caso de necesitar que el servidor sea visible desde afuera de la LAN, debemos realizar un forwardeo al mismo puerto del 
servidor, en el router. Para esto, yo utilicé un herramienta llamada Miranda, la cual está hecha en python, para lograr esto.
Esta herramienta, permite reconocer los dispositivos cercanos que poseen el protocolo UPNP para conectarse con diversos tipos
de dispositivos. Explicaria como se usa, pero sinceramente hay muchos tutoriales que hablan de ello y es muy simple.

Solo me falta decir que una vez realizado el forwardeo del puerto del router a nuestra maquina con dicha herramienta u otra,
solo nos queda decirle a nuestro sistema operativo, o mejor dicho a su Firewall, que debe permitir las conexiones entrantes a
dicho puerto. En linux, el firewall se maneja mediante el comando IPTABLES, y por suerte, lograr nuestro objetivo consiste
en una sola linea que habra el puerto (lo pueden encontrar en internet, solo necesitan cambiar el puerto en la linea que van a
copiar y pegar jaja).

Cualquier cosa me consultan: darioblanca.lp@gmail.com
