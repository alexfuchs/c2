import paramiko
import os
import config1
import json


def set_config_key(key, value):
    globals()[key] = value


def connect(host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username='alex', password='1234')
    return client


def command(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    return stdout.readlines()


def main(database=None, api_key=None, base_url=None):
    with open("config.json") as json_config:
        for key, value in json.load(json_config).items():
            set_config_key(key, value)
    # color = print(config.server['color'])
    vm0_old = config1.server["vm0_old"]
    vm1_old = config1.server["vm1_old"]
    vm0_new = config1.server["vm0_new"]
    vm1_new = config1.server["vm1_new"]
    host_list_old = config1.server["host_list_old"]
    host_list_new = config1.server["host_list_new"]
    apptc = config1.app["apptc"]
    appweb = config1.app["appweb"]
    # print(color, vm1, vm2, host_list)
    print("vm0_old= ", vm0_old)
    print("vm1_old= ", vm1_old)
    print("vm0_new= ", vm0_new)
    print("vm1_new= ", vm0_new)
    print("host_list_old= ", host_list_old)
    print("host_list_new= ", host_list_new)
    print("apptc= ", apptc)

    client = connect('127.0.0.1')
    print(command(client, "ls -l /var/tmp/qq"))
    print(command(client, "whoami"))

    #client = connect("lnx9692k.eng.zkb.ch")
    #print(command(client, "hostname"))
    #print(command(client, "asroot systemctl status slbbteccme"))
    print()
    print("do this")
    print("systemctl status slbriskreport")
    print("systemctl status slbriskreportweb")
    print("/etc/rc.sm -r SLBRISK stop")
    print("/etc/rc.sm -r SLBRISKWEB stop")
    print("/etc/rc.sm -r SLBRISK reset")
    print("/etc/rc.sm -r SLBRISKWEB reset")
    print("grep ExecStop /usr/lib/systemd/system/slbriskexportwebip.service")
    print("grep ExecStop /usr/lib/systemd/system/slbriskexportip.service")

    print(database)
    print(api_key)
    print(base_url)


if __name__ == "__main__":
    main()
