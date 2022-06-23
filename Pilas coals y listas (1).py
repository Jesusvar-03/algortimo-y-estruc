import queue 

q = queue.Queue()

q.put("Mario");
q.put("Bryan");
q.put("Daniel");

a = 2
a = input("Esta es la cola de espera ¿Que desea hacer? (a)Agregar otro paciente  (b) Cuantos pacientes faltan  (c) El proximo paciente en pasar: ")
if a == 'a':
    q.put(str(input("Agregue el paciente: ")))
elif a == 'b':
    print(q.qsize())
elif a == 'c':
    print(q.get())
else:
    print("Are you serious?")