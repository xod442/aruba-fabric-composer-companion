from pyhpecfm.client import CFMClient
from pyhpecfm import fabric

ipaddress = '172.18.1.66'
username = 'admin'
password = 'plexxi'

client = CFMClient(ipaddress, username, password)
client.connect()

params={'count_only': False,
         'mac_attachemnts': False,
         'mac_learning': True,
         'ports': True,
         'port_type': 'access',
         'tag': True,
         'type': 'provisioned',
         'vlan_groups': True
         }
cfm_lags=fabric.get_lags(client,params)
print cfm_lags
