from utilities.get_ifdesc import get_ifDesc_oids
from utilities.get_iftype import get_ifType_oids
from utilities.get_ifmtu import get_ifMtu_oids
from utilities.get_ifspeed import get_ifSpeed_oids
from utilities.get_ifphysaddress import get_ifPhysAddress_oids
from utilities.get_ifadminstatus import get_ifAdminStatus_oids
from utilities.get_ifoperstatus import get_ifOperStatus_oids
from utilities.get_ifinucastpkts import get_ifInUcastPkts_oids
from utilities.get_ifinerror import get_ifInError_oids
from utilities.get_ifoutucastpkts import get_ifOutUcastPkts_oids
from utilities.get_ifouterror import get_ifOutError_oids


oid = '1.3.6.1.2.1.2.2.1.2.8'
ipaddress='172.18.31.1'
#
ifDesc=get_ifDesc_oids(ipaddress)
ifType=get_ifType_oids(ipaddress)
ifMtu=get_ifMtu_oids(ipaddress)
ifSpeed=get_ifSpeed_oids(ipaddress)
#ifPhysAddress=get_ifPhysAddress_oids(ipaddress)
ifAdminStatus=get_ifAdminStatus_oids(ipaddress)
ifOperStatus=get_ifOperStatus_oids(ipaddress)
ifInUcastPkts=get_ifInUcastPkts_oids(ipaddress)
#ifInError=get_ifInError_oids(ipaddress)
ifOutUcastPkts=get_ifOutUcastPkts_oids(ipaddress)
#ifOutError=get_ifOutError_oids(ipaddress)



#print ifDesc
#print ifType
#print ifMtu
#print ifSpeed
#print ifPhysAddress
#print ifAdminStatus
#print ifOperStatus
#print ifInUcastPkts
##print ifInError
#print ifOutUcastPkts
#print ifOutError
counter=0
while counter < len(ifDesc):

    interface={'Interface':counter+1,
               'ifDesc':ifDesc[counter],
               'ifType':ifType[counter],
               'ifMtu':ifMtu[counter],
               'ifSpeed':ifSpeed[counter],
               'ifAdminStatus':ifAdminStatus[counter],
               'ifOperStatus':ifOperStatus[counter],
               'ifInUcastPkts': ifInUcastPkts[counter],
               'ifOutUcastPkts':ifOutUcastPkts[counter]
               }

    print interface
    counter=counter+1
