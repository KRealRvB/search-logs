import telnetlib
import time
from pprint import pprint
from subprocess import Popen, PIPE

username = "admin"
password = ",kjibysqhsyjr"


def to_bytes(line):
    return f"{line}\n".encode("utf-8")

# def send_show_command(ip, username, password, enable, commands):
#     with telnetlib.Telnet(ip) as telnet:
#         telnet.read_until(b":")
#         telnet.write(to_bytes(username))
#         telnet.read_until(b":")
#         telnet.write(to_bytes(password))
#         m, output = telnet.expect([b"#"])
#         telnet.write(b"show vlan port 1\n")
#         print(telnet.read_all())
            
with telnetlib.Telnet('10.10.0.114') as telnet:
    telnet.read_until(b":")
    telnet.write(to_bytes(username))
    telnet.read_until(b":")
    telnet.write(to_bytes(password))
    telnet.read_until(b"#")
    telnet.write(to_bytes('show log'))
    time.sleep(10)
    base = (telnet.read_very_eager().decode('utf-8'))
print(base)
