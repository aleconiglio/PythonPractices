import urllib.request
import common
import tcp



port = 5000

my_ip = urllib.request.urlopen("https://api.ipify.org").read().decode("utf-8")

personal_id = my_ip + ":" + str(port)

base64_str = common.str_base64(personal_id)
print("My id -> "+ base64_str)

send = input("Send(1) or receive(0)? :")

if send == "1":
    dest_id = input("address: ")
    who = common.base64_str(dest_id)
    print(who)
    file_path = input("path file pls: ")
    file = open(file_path, 'rb')

    tcp.send_file(who, file)
    quit()
print("end")


