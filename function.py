import netmiko

from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type="cisco_xe",
    host="cisco5.domain.com",
    username="admin",
    password="password",
)

connection

output = connection.send_command("show ip interface brief")
print(output)


