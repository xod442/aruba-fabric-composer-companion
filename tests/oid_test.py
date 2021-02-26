from utilities.get_one_oid import get_oid

# Get number of interfaces.
total_interfaces='1.3.6.1.2.1.2.1.0'
try:
    result = get_oid(total_interfaces)
except:
    error='failure getting number of interfaces via snmp'
    print error

total_interfaces=int(result)


# Get ifIndex - where do the interfaces start in snmp.
ifIndex='1.3.6.1.2.1.2.2.1.1.4'
try:
    result = get_oid(ifIndex)
    print'---------------------------------------------'
    print result
    print'---------------------------------------------'
except:
    error='failure getting number of interfaces via snmp'
    print error

index=int(result)
print 'This is ifIndex: '+str(index)

interfaces={'ifIndex': index,'total_interfaces': total_interfaces}
print total_interfaces
interface_detail=[]
interface=1
list_track=0
ifDesc='1.3.6.1.2.1.2.2.1.2.'
ifType='1.3.6.1.2.1.2.2.1.3.'
ifMtu='1.3.6.1.2.1.2.2.1.4.'
ifSpeed='1.3.6.1.2.1.2.2.1.5.'
ifPhysAddress='1.3.6.1.2.1.2.2.1.6.'
ifAdminStatus='1.3.6.1.2.1.2.2.1.7.'
ifInUcastPkts='1.3.6.1.2.1.2.2.1.11.'
ifInErrors='1.3.6.1.2.1.2.2.1.14.'
ifOutUcastPkts='1.3.6.1.2.1.2.2.1.17.'
ifOutErrors='1.3.6.1.2.1.2.2.1.20.'
oid_list=[ifDesc]
#oid_list=[ifDesc,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifInUcastPkts,ifInErrors,ifOutUcastPkts,ifOutErrors]
oid_names=['ifDesc','ifType','ifMtu','ifSpeed','ifPhysAddress','ifAdminStatus','ifInUcastPkts','ifInErrors','ifOutUcastPkts','ifOutErrors']
print interfaces
print oid_list
print oid_names
ports=[]

# Process OID's
for oid in oid_list:
    while interface <= total_interfaces:
        new_oid=oid+str(index)
        result=get_oid(new_oid)
        print result
        dex=str(result)
        interface_name='interface'+str(interface)
        print 'this is the name: '+ interface_name
        ports={'interface':interface,'ifDesc':dex}

        interface_detail.append(ports)
        print interface_detail

        interface=interface+1
        index=index+1
