import socket
def sendstxt(): #Функция для принятия сообщений
  data=conn.recv(1024)
  print(data.decode())   
f=open('O:\Факультет ПМиИТ\ПИ18-4\Фарбовская Светлана Сергеевна - 182753\Unix\txt.txt','w') #Фаил со служебными сообщениями 
names=open('O:\Факультет ПМиИТ\ПИ18-4\Фарбовская Светлана Сергеевна - 182753\Unix\names.txt','rw') #Фаил с именами
f.write("Открываем сервер")
sock = socket.socket()
 
while True:

    
 i=9093
 sock.bind(("",i))
 f.write("Прослушиваем порт")
 try:
     sock.listen(1)
 except:
     while True:
      i=i+1
      sock.bind(("",i))
 print("Номер порта:",i)
 
      
    
 f.write("Подключаем клиента")
 while True: #многопользовательский чат
   conn, addr = sock.accept()
   for lines in names: #моя странная реализация кукки
       if lines[1]==conn:
         print('Hello', lines[2])
         password=input("Enter your password:")
         while (password != lines[3]):
             password=str(input(lines[2]," Your password is wrong. Enter it again:"))
             i=1
   if i==0:
       names.write(input("Enter your name:"))
       password=str(input("Enter your password:"))
       password2=str(input("Enter your password again:"))
       while (password!=password2):
           password2=str(input("Error. Passwords in not shodatsya! Enter your password again:"))
       names.write(password)
  

  f.write("Принемаем данные от клиента")
  data=conn.recv(1024)
  print(data.decode())
  if (data.decode() == "Exit"):
      f.write("Отключаем клиента. Пока-пока")
      conn.close

  conn.sendstxt #выполняем функцию принятия сообщений от клиента

  f.write("Отправляем данные клиенту")
  conn.send(b"hi")
  conn.send(('\nIP {}'.format(addr[0])).encode())
  f.write("Стопаем сервак")



f.close()
names.close()
sock.close
