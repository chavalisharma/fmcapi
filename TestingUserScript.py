"""
Unit testing, of a sort, all the created methods/classes.
"""

from fmcapi.fmc import *
from fmcapi.api_objects import *
from fmcapi.helper_functions import *
import logging
import time
import pprint

# ### Set these variables to match your environment. ### #

host = 'fmclab.tor.afilias-int.info'
username = 'apiscript'
password = 'XXXXXXXX'
autodeploy = False


# ### These functions are the individual tests you can run to ensure functionality. ### #


def test__url_category():
    logging.info('# Testing URLCategory class.')
    obj1 = URLCategory(fmc=fmc1)
    print('All URLCategories -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = URLCategory(fmc=fmc1, name='SPAM URLs')
    print('One URLCategory -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing URLCategory class done.\n')


def test__ports():
    logging.info('# Test Ports.  This only returns a full list of various Port object types.')
    obj1 = Ports(fmc=fmc1)
    print('Ports -->')
    result = obj1.get()
    pp.pprint(result)
    print('\n')
    logging.info('# Test Ports done.\n')


def test__application_type():
    logging.info('# Testing ApplicationType class.')
    obj1 = ApplicationType(fmc=fmc1)
    print('All ApplicationType -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = ApplicationType(fmc=fmc1, name='Server')
    print('One ApplicationType -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing ApplicationType class done.\n')


def test__application_tag():
    logging.info('# Testing ApplicationTag class.')
    obj1 = ApplicationTag(fmc=fmc1)
    print('All ApplicationTag -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = ApplicationTag(fmc=fmc1, name='file sharing/transfer')
    print('One ApplicationTag -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing ApplicationTag class done.\n')


def test__application():
    logging.info('# Testing Application class.')
    obj1 = Application(fmc=fmc1)
    print('### Warning, this query takes a LONG time to process.  Watch the output.log file for regular updates. ###')
    print('All Application -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = Application(fmc=fmc1, name='WD softwares Download/Update')
    print('### Warning, this query takes a LONG time to process.  Watch the output.log file for regular updates. ###')
    print('One Application -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing Application class done.\n')


def test__application_risk():
    logging.info('# Testing ApplicationRisk class.')
    obj1 = ApplicationRisk(fmc=fmc1)
    print('All ApplicationRisks -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = ApplicationRisk(fmc=fmc1, name='Very High')
    print('One ApplicationRisk -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing ApplicationRisk class done.\n')


def test__application_productivity():
    logging.info('# Testing ApplicationProductivity class.')
    obj1 = ApplicationProductivity(fmc=fmc1)
    print('All ApplicationProductivities -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = ApplicationProductivity(fmc=fmc1, name='Very Low')
    print('One ApplicationProductivity -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing ApplicationProductivity class done.\n')


def test__application_category():
    logging.info('# Testing ApplicationCategory class.')
    obj1 = ApplicationCategory(fmc=fmc1)
    print('All ApplicationCategories -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = ApplicationCategory(fmc=fmc1, name='SMS tools')
    print('One ApplicationCategory -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing ApplicationCategory class done.\n')


def test__country():
    logging.info('# Testing Country class.')
    obj1 = Country(fmc=fmc1)
    print('All Countries -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = Country(fmc=fmc1, name='Isle Of Man')
    print('One Country -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing Country class done.\n')


def test__continent():
    logging.info('# Testing Continent class.')
    obj1 = Continent(fmc=fmc1)
    print('All Continents -- >')
    result = obj1.get()
    pp.pprint(result)
    print("Total items: {}".format(len(result['items'])))
    print('\n')
    del obj1
    obj1 = Continent(fmc=fmc1, name='North America')
    print('One Continent -- >')
    pp.pprint(obj1.get())
    print('\n')
    logging.info('# Testing Continent class done.\n')


def test__vlan_group_tag():
    logging.info('# Testing VlanGroupTag class.')
    obj10 = VlanTag(fmc=fmc1, name='_vlantag10', data={'startTag': '888', 'endTag': '999'})
    obj10.post()
    obj11 = VlanTag(fmc=fmc1, name='_vlantag11', data={'startTag': '222', 'endTag': '333'})
    obj11.post()
    obj12 = VlanTag(fmc=fmc1, name='_vlantag12', data={'startTag': '1', 'endTag': '999'})
    obj12.post()
    time.sleep(1)
    obj1 = VlanGroupTag(fmc=fmc1, name=namer)
    obj1.named_vlantags(action='add', name=obj10.name)
    obj1.named_vlantags(action='add', name=obj11.name)
    obj1.named_vlantags(action='remove', name=obj11.name)
    obj1.named_vlantags(action='clear')
    obj1.named_vlantags(action='add', name=obj10.name)
    obj1.named_vlantags(action='add', name=obj11.name)
    obj1.named_vlantags(action='add', name=obj12.name)
    obj1.named_vlantags(action='remove', name=obj12.name)
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = VlanGroupTag(fmc=fmc1, name=namer)
    obj1.get()
    obj1.unnamed_vlantags(action='add', startvlan='22', endvlan='33')
    obj1.unnamed_vlantags(action='clear')
    obj1.unnamed_vlantags(action='add', startvlan='22', endvlan='33')
    obj1.unnamed_vlantags(action='remove', startvlan='22', endvlan='33')
    obj1.unnamed_vlantags(action='add', startvlan='44', endvlan='33')
    obj1.unnamed_vlantags(action='add', startvlan='900')
    obj1.put()
    time.sleep(1)
    obj1.delete()
    obj10.delete()
    obj11.delete()
    obj12.delete()
    logging.info('# Testing VlanGroupTag class done.\n')


def test__url_group():
    logging.info('# Testing URLGroup class.')
    url1 = URL(fmc=fmc1, name='_url1', url='example.org')
    url1.post()
    url2 = URL(fmc=fmc1, name='_url2', url='example.net')
    url2.post()
    url3 = URL(fmc=fmc1, name='_url3', url='example.com')
    url3.post()
    time.sleep(1)
    obj1 = URLGroup(fmc=fmc1, name=namer)
    obj1.named_urls(action='add', name=url1.name)
    obj1.named_urls(action='add', name=url1.name)
    obj1.named_urls(action='clear')
    obj1.named_urls(action='add', name=url2.name)
    obj1.named_urls(action='add', name=url3.name)
    obj1.named_urls(action='add', name=url1.name)
    obj1.named_urls(action='remove', name=url3.name)
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = URLGroup(fmc=fmc1, name=namer)
    obj1.get()
    obj1.unnamed_urls(action='add', value='daxm.net')
    obj1.unnamed_urls(action='add', value='daxm.com')
    obj1.unnamed_urls(action='clear')
    obj1.unnamed_urls(action='add', value='daxm.org')
    obj1.unnamed_urls(action='add', value='daxm.net')
    obj1.unnamed_urls(action='add', value='daxm.lan')
    obj1.unnamed_urls(action='remove', value='daxm.org')
    obj1.put()
    time.sleep(1)
    obj1.delete()
    url1.delete()
    url2.delete()
    url3.delete()
    logging.info('# Testing URLGroup class done.\n')


def test__network_group():
    logging.info('# Testing NetworkGroup class.')
    obj10 = IPHost(fmc=fmc1, name='_iphost1', value='3.3.3.3')
    obj10.post()
    obj11 = IPNetwork(fmc=fmc1, name='_ipnet1', value='3.3.3.0/24')
    obj11.post()
    obj12 = IPRange(fmc=fmc1, name='_iprange1', value='3.3.3.3-33.33.33.33')
    obj12.post()
    time.sleep(1)
    obj1 = NetworkGroup(fmc=fmc1, name=namer)
    obj1.named_networks(action='add', name=obj10.name)
    obj1.named_networks(action='add', name=obj10.name)
    obj1.named_networks(action='remove', name=obj10.name)
    obj1.named_networks(action='clear')
    obj1.named_networks(action='add', name=obj11.name)
    obj1.named_networks(action='add', name=obj12.name)
    obj1.named_networks(action='remove', name=obj11.name)
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = NetworkGroup(fmc=fmc1, name=namer)
    obj1.get()
    obj1.unnamed_networks(action='add', value='1.2.3.4')
    obj1.unnamed_networks(action='clear')
    obj1.unnamed_networks(action='add', value='1.2.3.4')
    obj1.unnamed_networks(action='remove', value='1.2.3.4')
    obj1.unnamed_networks(action='add', value='6.7.8.9')
    obj1.unnamed_networks(action='add', value='1.2.3.0/24')
    obj1.post()
    time.sleep(1)
    obj1.delete()
    obj10.delete()
    obj11.delete()
    obj12.delete()
    logging.info('# Testing NetworkGroup class done.\n')


def test__ip_addresses():
    logging.info('# Test IPAddresses.  This only returns a full list of IP object types.')
    obj1 = IPAddresses(fmc=fmc1)
    print('IPAddresses -->')
    result = obj1.get()
    pp.pprint(result)
    print('\n')
    logging.info('# Test IPAddresses done.\n')


def test__fmc_version():
    logging.info('# Testing fmc.version() method.  Getting version information information from FMC.')
    version_info = fmc1.version()
    print('fmc.version() -- >')
    pp.pprint(version_info)
    print('\n')
    logging.info('# Testing fmc.verson() done.')


def test__variable_set():
    logging.info('# Test VariableSet. Can only GET VariableSet objects.')
    obj1 = VariableSet(fmc=fmc1)
    obj1.get(name='Default-Set')
    print('VariableSet -->')
    pp.pprint(obj1.format_data())
    print('\n')
    logging.info('# Test VariableSet done.\n')


def test__ip_host():
    logging.info('# Test IPHost.  Post, get, put, delete Host Objects.')
    obj1 = IPHost(fmc=fmc1)
    obj1.name = namer
    obj1.value = '8.8.8.8/32'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = IPHost(fmc=fmc1, name=namer)
    obj1.get()
    obj1.value = '9.9.9.9'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test IPHost done.\n')


def test__ip_network():
    logging.info('# Test IPNetwork.  Post, get, put, delete Network Objects.')
    obj1 = IPNetwork(fmc=fmc1)
    obj1.name = namer
    obj1.value = '8.8.8.0/24'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = IPNetwork(fmc=fmc1, name=namer)
    obj1.get()
    obj1.value = '9.9.9.0/24'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test IPNetwork done.\n')


def test__ip_range():
    logging.info('# Test IPRange.  Post, get, put, delete Range Objects.')
    obj1 = IPRange(fmc=fmc1)
    obj1.name = namer
    obj1.value = '1.1.1.1-2.2.2.2'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = IPRange(fmc=fmc1, name=namer)
    obj1.get()
    obj1.value = '3.3.3.3-4.4.4.4'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test IPRange done.\n')


def test__url():
    logging.info('# Test URL.  Post, get, put, delete URL Objects.')
    obj1 = URL(fmc=fmc1)
    obj1.name = namer
    obj1.url = 'daxm.com'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = URL(fmc=fmc1, name=namer)
    obj1.get()
    obj1.url = 'daxm.lan'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test URL done.\n')


def test__vlan_tag():
    logging.info('# Test VlanTag.  Post, get, put, delete VLAN Tag Objects.')
    obj1 = VlanTag(fmc=fmc1)
    obj1.name = namer
    obj1.vlans(start_vlan='100', end_vlan='200')
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = VlanTag(fmc=fmc1, name=namer)
    obj1.get()
    obj1.vlans(start_vlan='400', end_vlan='300')
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test VlanTag done.\n')


def test__protocol_port():
    logging.info('# Test ProtocolPort.  Post, get, put, delete Port Objects.')
    obj1 = ProtocolPort(fmc=fmc1)
    obj1.name = namer
    obj1.port = '1234'
    obj1.protocol = 'TCP'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = ProtocolPort(fmc=fmc1, name=namer)
    obj1.get()
    obj1.port = '5678'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test ProtocolPort done.\n')


def test__security_zone():
    logging.info('# Test SecurityZone.  Post, get, put, delete Security Zone Objects.')
    obj1 = SecurityZone(fmc=fmc1)
    obj1.name = namer
    obj1.interfaceMode = 'ROUTED'
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = SecurityZone(fmc=fmc1, name=namer)
    obj1.get()
    obj1.name = 'DEMO'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test SecurityZone done.\n')


def test__interface_group():
    logging.info('# Test InterfaceGroup.  Post, get, put, delete InterfaceGroup Objects.')
    obj1 = InterfaceGroup(fmc=fmc1)
    obj1.name = "_ig_outside_all"
    obj1.interfaceMode = 'ROUTED'
    print('InterfaceGroup POST-->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.post()
    time.sleep(1)
    del obj1

    obj1 = InterfaceGroup(fmc=fmc1, name="_ig_outside_all")
    obj1.get()
    obj1.p_interface(device_name="FTDv03.ccie.lab", action="add",
                     names=["GigabitEthernet0/0", "GigabitEthernet0/1", "GigabitEthernet0/2"])
    print('InterfaceGroup PUT-->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.put()
    time.sleep(1)
    del obj1

    obj1 = InterfaceGroup(fmc=fmc1, name="_ig_outside_all")
    obj1.get()
    obj1.p_interface(device_name="FTDv03.ccie.lab", action="remove", names=["GigabitEthernet0/1"])
    print('InterfaceGroup PUT-->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.put()
    time.sleep(1)
    del obj1

    obj1 = InterfaceGroup(fmc=fmc1, name="_ig_outside_all")
    obj1.get()
    obj1.p_interface(action="clear-all")
    obj1.put()
    print('InterfaceGroup DELETE-->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.delete()
    del obj1
    logging.info('# Test InterfaceGroup done.\n')


def test__slamonitor():
    logging.info('# Test SLAMonitor.  Post, get, put, delete SLAMonitor Objects.')
    sz1 = SecurityZone(fmc=fmc1)
    sz1.name = "SZ-OUTSIDE1"
    sz1.interfaceMode = 'ROUTED'
    sz1.post()
    time.sleep(1)

    sz2 = SecurityZone(fmc=fmc1)
    sz2.name = "SZ-OUTSIDE2"
    sz2.interfaceMode = 'ROUTED'
    sz2.post()
    time.sleep(1)

    obj1 = SLAMonitor(fmc=fmc1)
    obj1.name = namer
    obj1.frequency = 30
    obj1.slaId = 1
    obj1.monitorAddress = "8.8.8.7"
    obj1.timeout = 5000
    obj1.threshold = 2
    obj1.noOfPackets = 1
    obj1.dataSize = 28
    obj1.tos = 1
    obj1.interfaces(names=["SZ-OUTSIDE1", "SZ-OUTSIDE2"])
    obj1.post()
    print('SLAMonitor Post -->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.get(name=namer)
    obj1.monitorAddress = "8.8.8.8"
    obj1.put()
    print('SLAMonitor Put -->')
    pp.pprint(obj1.format_data())
    print('\n')
    time.sleep(1)
    obj1.delete()
    sz1.delete()
    sz2.delete()


def test__device():
    logging.info('# Test Device.  Though you can "Post" devices I do not have one handy. So '
                 'add/remove licenses on Device Objects.')
    acp1 = AccessControlPolicy(fmc=fmc1, name=namer)
    acp1.post()
    obj1 = Device(fmc=fmc1)
    obj1.name = namer
    obj1.acp(name=acp1.name)
    obj1.licensing(action='add', name='MALWARE')
    obj1.licensing(action='add', name='VPN')
    obj1.licensing(action='remove', name='VPN')
    obj1.licensing(action='clear')
    obj1.licensing(action='add', name='BASE')
    print('Device -->')
    pp.pprint(obj1.format_data())
    print('\n')
    acp1.delete()
    logging.info('# Test Device done.\n')


def test__device_with_task():
    logging.info('# Test Device1 with Task.  This requires having an actual device with the "configure manager add" '
                 'statement enabled.')
    acp1 = AccessControlPolicy(fmc=fmc1, name=namer)
    acp1.post()

    starttime = str(int(time.time()))
    obj1_namer = '_fmcapi_test_{}'.format(starttime)

    obj1 = Device(fmc=fmc1)
    obj1.hostName = "10.255.0.43"
    obj1.name = obj1_namer
    obj1.regKey = "cisco123"
    obj1.natID = "cisco123"
    obj1.acp(name=acp1.name)
    obj1.licensing(action='add', name='BASE')
    obj1.licensing(action='add', name='THREAT')
    obj1.licensing(action='add', name='MALWARE')
    print('Device -->')
    pp.pprint(obj1.format_data())
    print('\n')
    response = obj1.post()
    wait_for_task(response["metadata"]["task"], 30)
    logging.info('# Test Device2 with Task.  This requires having an actual device with the "configure manager add" '
                 'statement enabled.')

    starttime = str(int(time.time()))
    obj2_namer = '_fmcapi_test_{}'.format(starttime)

    obj2 = Device(fmc=fmc1)
    obj2.hostName = "10.255.0.44"
    obj2.name = obj2_namer
    obj2.regKey = "cisco123"
    obj2.natID = "cisco123"
    obj2.acp(name=acp1.name)
    obj2.licensing(action='add', name='BASE')
    obj2.licensing(action='add', name='THREAT')
    obj2.licensing(action='add', name='MALWARE')
    print('Device -->')
    pp.pprint(obj2.format_data())
    print('\n')
    response = obj2.post()
    wait_for_task(response["metadata"]["task"], 30)

    # Wait some additional time to complete device registration before deletion
    time.sleep(180)
    obj1 = Device(fmc=fmc1)
    obj2 = Device(fmc=fmc1)
    obj1.get(name=obj1_namer)
    obj2.get(name=obj2_namer)

    obj1.delete()
    time.sleep(30)
    obj2.delete()
    time.sleep(30)
    acp1.delete()


def test__phys_interfaces():
    logging.info('# Test PhysicalInterface.  get, put PhysicalInterface Objects. Requires registered device')
    sz1 = SecurityZone(fmc=fmc1)
    sz1.name = "SZ-OUTSIDE1"
    sz1.post()
    time.sleep(1)
    sz2 = SecurityZone(fmc=fmc1)
    sz2.name = "SZ-OUTSIDE2"
    sz2.post()
    time.sleep(1)

    intf1 = PhysicalInterface(fmc=fmc1, device_name="device-name")
    intf1.get(name="GigabitEthernet0/0")
    intf1.enabled = True
    intf1.ifname = "OUTSIDE1"
    intf1.activeMACAddress = "0050.5686.718f"
    intf1.standbyMACAddress = "0050.5686.0c2e"
    intf1.static(ipv4addr="10.254.0.3", ipv4mask=24)
    intf1.sz(name="SZ-OUTSIDE1")
    intf2 = PhysicalInterface(fmc=fmc1, device_name="device-name")
    intf2.get(name="GigabitEthernet0/1")
    intf2.enabled = True
    intf2.ifname = "OUTSIDE2"
    intf2.activeMACAddress = "0050.5686.821d"
    intf2.standbyMACAddress = "0050.5686.11cb"
    intf2.dhcp()
    intf2.sz(name="SZ-OUTSIDE2")
    intf1.put()
    time.sleep(1)
    intf2.put()
    time.sleep(1)
    intf1.get()
    intf2.get()

    intf1.enabled = False
    intf1.activeMACAddress = ""
    intf1.standbyMACAddress = ""
    intf1.static(ipv4addr="", ipv4mask="")
    intf1.securityZone = {}
    intf1.activeMACAddress = ""
    intf1.standbyMACAddress = ""
    intf2.enabled = False
    intf2.activeMACAddress = ""
    intf2.standbyMACAddress = ""
    intf2.static(ipv4addr="", ipv4mask="")
    intf2.securityZone = {}
    intf2.activeMACAddress = ""
    intf2.standbyMACAddress = ""
    intf1.put()
    time.sleep(1)
    intf2.put()
    time.sleep(1)
    intf1.get()
    intf2.get()
    intf1.ifname = ""
    intf2.ifname = ""
    intf1.put()
    sz1.delete()
    intf2.put()
    sz2.delete()


def test__device_ha_pair():
    logging.info('# Test DeviceHAPairs. After an HA Pair is created, all API calls to "devicerecords" objects should '
                 'be directed at the currently active device not the ha pair')
    failover1 = PhysicalInterface(fmc=fmc1)
    failover1.get(device_name="PrimaryName", name="GigabitEthernet0/6")
    stateful1 = PhysicalInterface(fmc=fmc1)
    stateful1.get(device_name="PrimaryName", name="GigabitEthernet0/7")
    obj1 = DeviceHAPairs(fmc=fmc1)
    obj1.primary(name="PrimaryName")
    obj1.secondary(name="SecondaryName")
    obj1.name = "HaName"
    # failover interface subnetMask must be in x.x.x.x format"
    obj1.ftdHABootstrap = {
        "isEncryptionEnabled": "true",
        "encKeyGenerationScheme": "CUSTOM",
        "sharedKey": "cisco123",
        "useSameLinkForFailovers": False,
        "lanFailover": {
            "useIPv6Address": False,
            "subnetMask": "255.255.255.252",
            "interfaceObject": {
                "type": "PhysicalInterface",
                "name": failover1.name,
                "id": failover1.id
            },
            "standbyIP": "192.168.1.2",
            "logicalName": "HA-FAILOVER",
            "activeIP": "192.168.1.1"
        },
        "statefulFailover": {
            "useIPv6Address": False,
            "subnetMask": "255.255.255.252",
            "interfaceObject": {
                "type": "PhysicalInterface",
                "name": stateful1.name,
                "id": stateful1.id
            },
            "standbyIP": "192.168.1.6",
            "logicalName": "HA-STATEFUL",
            "activeIP": "192.168.1.5"}}
    # response = ha_pair.post()
    # wait_for_task(response["metadata"]["task"], 30)
    print('Device HA-->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.post()
    time.sleep(300)
    del obj1

    obj1 = DeviceHAPairs(fmc=fmc1, name="HaName")
    obj1.switch_ha()
    print('Device HA Switch-->')
    pp.pprint(obj1.format_data())
    print('\n')
    response = obj1.put()
    print(response)
    time.sleep(20)
    del obj1

    obj1 = DeviceHAPairs(fmc=fmc1, name="HaName")
    obj1.break_ha()
    print('Device HA Break-->')
    pp.pprint(obj1.format_data())
    print('\n')
    response = obj1.put()
    print(response)

    # time.sleep(300)
    # del obj1
    # obj1 = DeviceHAPairs(fmc=fmc1)
    # obj1.get(name="FTDv-HA2")
    # Deleting the HAPair object will delete the HA configuration AND remove the devices from the FPMC
    # response = obj1.delete()


def test__device_ha_monitored_interfaces():
    logging.info('# Test DeviceHAMonitoredInterfaces. get, put DeviceHAMonitoredInterfaces Objects')
    obj1 = DeviceHAMonitoredInterfaces(fmc=fmc1, ha_name="HaName")
    # Interface logical name (ifname)
    obj1.get(name="OUTSIDE1")
    obj1.monitorForFailures = True
    obj1.ipv4(ipv4addr="10.254.0.4", ipv4mask=29, ipv4standbyaddr="10.254.0.3")
    print('DeviceHAMonitoredInterfaces PUT-->')
    pp.pprint(obj1.format_data())
    print('\n')
    print(obj1.put())


def test__device_ha_failover_mac():
    logging.info('# Test DeviceHAFailoverMAC. get, post, put, delete DeviceHAFailoverMAC Objects')
    obj1 = DeviceHAFailoverMAC(fmc=fmc1, ha_name="HaName")
    obj1.p_interface(name="GigabitEthernet0/0", device_name="device-name")
    obj1.failoverActiveMac = "0050.5686.718f"
    obj1.failoverStandbyMac = "1050.5686.0c2e"
    print('DeviceHAFailoverMAC POST->')
    pp.pprint(obj1.format_data())
    print('\n')
    obj1.post()
    del obj1

    obj1 = DeviceHAFailoverMAC(fmc=fmc1)
    obj1.edit(name="GigabitEthernet0/0", ha_name="HaName")
    obj1.failoverStandbyMac = "0050.5686.0c2e"
    print('DeviceHAFailoverMAC PUT->')
    print('\n')
    pp.pprint(obj1.format_data())
    del obj1

    obj1 = DeviceHAFailoverMAC(fmc=fmc1)
    obj1.edit(name="GigabitEthernet0/0", ha_name="ftdv03")
    obj1.delete()


def test__intrusion_policy():
    logging.info('# Test IntrusionPolicy. Can only GET IntrusionPolicy objects.')
    obj1 = IntrusionPolicy(fmc=fmc1)
    obj1.get(name='Security Over Connectivity')
    print('IntrusionPolicy -->')
    pp.pprint(obj1.format_data())
    print('\n')
    logging.info('# Test IntrusionPolicy done.\n')


def test__access_control_policy():
    logging.info('# Test AccessControlPolicy.  Post, get, put, delete ACP Objects.')
    obj1 = AccessControlPolicy(fmc=fmc1)
    obj1.name = namer
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = AccessControlPolicy(fmc=fmc1, name=namer)
    obj1.get()
    obj1.name = 'asdfasdf'
    obj1.put()
    time.sleep(1)
    obj1.delete()
    logging.info('# Test AccessControlPolicy done.\n')


def test__acp_rule():
    logging.info('# In preparation for testing ACPRule methods, set up some known objects in the FMC.')
    # Build an IP host object
    iphost1 = IPHost(fmc=fmc1, name='_iphost1', value='7.7.7.7')
    iphost1.post()
    # Build an IP Network object
    ipnet1 = IPNetwork(fmc=fmc1, name='_ipnet1', value='1.2.3.0/24')
    ipnet1.post()
    # Build an IP range object
    iprange1 = IPRange(fmc=fmc1, name='_iprange1', value='6.6.6.6-7.7.7.7')
    iprange1.post()
    # Build a Network Group object
    ipnet2 = IPNetwork(fmc=fmc1, name='_ipnet2', value='5.5.5.0/24')
    ipnet2.post()
    time.sleep(1)
    obj1 = NetworkGroup(fmc=fmc1, name='_fmcapi_test_networkgroup')
    obj1.named_networks(action='add', name=ipnet2.name)
    obj1.unnamed_networks(action='add', value='4.4.4.4/32')
    obj1.post()
    # Build a URL object
    url1 = URL(fmc=fmc1, name='_url1', url='asdf.org')
    url1.post()
    # Build a VLAN Tag object
    vlantag1 = VlanTag(fmc=fmc1, name='_vlantag1', data={'startTag': '888', 'endTag': '999'})
    vlantag1.post()
    # Build a Port object
    pport1 = ProtocolPort(fmc=fmc1, name='_pport1', port='9090', protocol='UDP')
    pport1.post()
    # Build a Port Group Object
    obj10 = ProtocolPort(fmc=fmc1, name='_porttcp1', port='8443', protocol='TCP')
    obj10.post()
    obj11 = ProtocolPort(fmc=fmc1, name='_portudp1', port='161', protocol='UDP')
    obj11.post()
    obj12 = ProtocolPort(fmc=fmc1, name='_portrangetcp1', port='0-1023', protocol='TCP')
    obj12.post()
    obj2 = PortObjectGroup(fmc=fmc1, name='_fmcapi_test_portobjectgroup')
    obj2.named_ports(action='add', name=obj10.name)
    obj2.named_ports(action='add', name=obj11.name)
    obj2.named_ports(action='add', name=obj12.name)
    obj2.post()
    # Build a Security Zone object
    sz1 = SecurityZone(fmc=fmc1, name='_sz1', interfaceMode='ROUTED')
    sz1.post()
    # Build an ACP Object
    acp1 = AccessControlPolicy(fmc=fmc1, name=namer)
    acp1.post()
    time.sleep(1)
    logging.info('# Setup of objects for ACPRule test done.\n')

    logging.info('# Test ACPRule.  Try to test all features of all methods of the ACPRule class.')
    acprule1 = ACPRule(fmc=fmc1, acp_name=acp1.name)
    acprule1.name = namer
    acprule1.action = 'ALLOW'
    acprule1.enabled = False
    acprule1.sendEventsToFMC = True
    acprule1.logFiles = False
    acprule1.logBegin = True
    acprule1.logEnd = True
    acprule1.variable_set(action='set', name='Default-Set')
    acprule1.source_zone(action='add', name=sz1.name)
    acprule1.destination_zone(action='add', name=sz1.name)
    acprule1.intrusion_policy(action='set', name='Security Over Connectivity')
    acprule1.vlan_tags(action='add', name=vlantag1.name)
    acprule1.source_port(action='add', name=pport1.name)
    acprule1.destination_port(action='add', name=pport1.name)
    acprule1.destination_port(action='add', name=obj2.name)
    acprule1.source_network(action='add', name=iphost1.name)
    acprule1.source_network(action='add', name=obj1.name)
    acprule1.source_network(action='add', name=iprange1.name)
    acprule1.destination_network(action='add', name=ipnet1.name)
    acprule1.destination_network(action='add', name=iprange1.name)
    acprule1.post()
    logging.info('# Test ACPRule done.\n')

    logging.info('# Cleanup of testing ACPRule methods.')
    acprule1.delete()
    time.sleep(1)
    acp1.delete()
    iphost1.delete()
    ipnet1.delete()
    iprange1.delete()
    obj1.delete()
    ipnet2.delete()
    url1.delete()
    vlantag1.delete()
    pport1.delete()
    sz1.delete()
    obj2.delete()
    obj10.delete()
    obj11.delete()
    obj12.delete()
    logging.info('# Cleanup of objects for ACPRule test done.\n')


def test__audit():
    logging.info('# Testing fmc.audit() method.')
    pp.pprint(fmc1.audit())
    logging.info('# Testing fmc.audit() method done.\n')


def test__port_object_group():
    logging.info('# Testing PortObjectGroup class.')
    obj10 = ProtocolPort(fmc=fmc1, name='_porttcp1', port='8443', protocol='TCP')
    obj10.post()
    obj11 = ProtocolPort(fmc=fmc1, name='_portudp1', port='161', protocol='UDP')
    obj11.post()
    obj12 = ProtocolPort(fmc=fmc1, name='_portrangetcp1', port='0-1023', protocol='TCP')
    obj12.post()
    time.sleep(1)
    obj1 = PortObjectGroup(fmc=fmc1, name=namer)
    obj1.named_ports(action='add', name=obj10.name)
    obj1.named_ports(action='add', name=obj10.name)
    obj1.named_ports(action='remove', name=obj10.name)
    obj1.named_ports(action='clear')
    obj1.named_ports(action='add', name=obj11.name)
    obj1.named_ports(action='add', name=obj12.name)
    obj1.named_ports(action='remove', name=obj11.name)
    obj1.post()
    time.sleep(1)
    del obj1
    obj1 = PortObjectGroup(fmc=fmc1, name=namer)
    obj1.get()
    obj1.named_ports(action='add', name='HTTP')
    obj1.named_ports(action='clear')
    obj1.named_ports(action='add', name='HTTP')
    obj1.named_ports(action='remove', name='HTTP')
    obj1.named_ports(action='add', name='HTTP')
    obj1.named_ports(action='add', name='HTTPS')
    obj1.put()
    time.sleep(1)
    obj1.delete()
    obj10.delete()
    obj11.delete()
    obj12.delete()
    logging.info('# Testing PortObjectGroup class done.\n')


def test__autonat():
    logging.info('# Testing FTDNatPolicy class.')
    # Create a container policy for FTD NAT rules
    natpol1 = FTDNatPolicy(fmc=fmc1, name=namer)
    natpol1.post()
    natpol1.get()

    # Create original and translate objects
    obj1 = IPNetwork(fmc=fmc1)
    obj1.name = 'net_original'
    obj1.value = '10.0.0.0/8'
    obj1.post()
    time.sleep(1)

    obj2 = IPHost(fmc=fmc1)
    obj2.name = 'net_xlate'
    obj2.value = '192.0.2.1'
    obj2.post()
    time.sleep(1)

    # Create identity nat object
    obj3 = IPNetwork(fmc=fmc1)
    obj3.name = 'net_identity'
    obj3.value = '192.168.0.0/24'
    obj3.post()
    time.sleep(1)

    # Create nat pool objects
    obj4 = IPNetwork(fmc=fmc1)
    obj4.name = 'net_original_pool'
    obj4.value = '172.16.0.0/24'
    obj4.post()
    time.sleep(1)

    # PAT Pool must be a range, not a subnet
    obj5 = IPRange(fmc=fmc1)
    obj5.name = 'net_xlate_pool'
    obj5.value = '192.0.2.128-192.0.2.254'
    obj5.post()
    time.sleep(1)

    # Create interface PAT object
    obj6 = IPNetwork(fmc=fmc1)
    obj6.name = 'net_original_intf'
    obj6.value = '192.168.1.0/24'
    obj6.post()
    time.sleep(1)

    # Autonat a network object to a host
    autonat1 = AutoNatRules(fmc=fmc1)
    autonat1.original_network(name="net_original")
    autonat1.translated_network(name="net_xlate")
    autonat1.natType = "STATIC"
    # Source and destination interface can be either an interface group or security zone
    autonat1.source_intf(name="IG-INSIDE")
    autonat1.destination_intf(name="SZ-OUTSIDE1")
    autonat1.nat_policy(name=namer)

    # Autonat identity nat
    autonat2 = AutoNatRules(fmc=fmc1)
    autonat2.identity_nat(name="net_identity")
    autonat2.source_intf(name="IG-INSIDE")
    autonat2.destination_intf(name="SZ-OUTSIDE1")
    autonat2.nat_policy(name=namer)

    # Autonat nat pool
    autonat3 = AutoNatRules(fmc=fmc1)
    autonat3.original_network(name="net_original_pool")
    autonat3.patPool(name="net_xlate_pool")
    autonat3.source_intf(name="IG-INSIDE")
    autonat3.destination_intf(name="SZ-OUTSIDE1")
    autonat3.nat_policy(name=namer)

    # Autonat interface PAT
    autonat4 = AutoNatRules(fmc=fmc1)
    autonat4.original_network(name="net_original_intf")
    autonat4.natType = "DYNAMIC"
    autonat4.source_intf(name="IG-INSIDE")
    autonat4.destination_intf(name="SZ-OUTSIDE1")
    autonat4.nat_policy(name=namer)
    autonat4.interfaceInTranslatedNetwork = True

    autonat1.post()
    autonat2.post()
    autonat3.post()
    autonat4.post()

    # Associate a nat policy to a device
    # Do not uncomment if you do not have a device registered to FPMC
    # Use name of device or deviceHAPair as applicable
    pol_devices = [{"name": "deviceHAName", "type": "deviceHAPair"}]
    assign1 = PolicyAssignments(fmc=fmc1)
    assign1.ftd_natpolicy(name=namer, devices=pol_devices)
    assign1.post()

    assign1.ftd_natpolicy(name=namer, devices=[])
    assign1.put()
    natpol1.delete()
    obj1.delete()
    obj2.delete()
    obj3.delete()
    obj4.delete()
    obj5.delete()
    obj6.delete()


def wait_for_task(task, wait_time=10):
    try:
        status = TaskStatuses(
            fmc=fmc1,
            id=task["id"],
            name=task["name"])
        current_status = status.get()
        '''
        Task Status for new device registration behaves differently than other tasks
        On new device registration, a task is sent for the initial registration. After completion 
        the UUID is deleted without any change in task status. So we check to see if the object no longer exists
        to assume the registration is complete.  After registration, discovery of the device begins, but there is
        no way to check for this with a task status.  The device can't be modified during this time, but a new device
        registration can begin.

        OTOH, a device HA operation will update its status to "Success" on completion.  Hence the two different checks.
        '''
        while current_status["status"] is not None and current_status["status"] != "Success":
            print("Task: %s %s %s" % (current_status["taskType"], current_status["status"], current_status["id"]))
            time.sleep(wait_time)
            current_status = status.get()
        print("Task: %s %s %s %s" % (current_status["taskType"], current_status["status"], current_status["id"]))
    except Exception as e:
        print(type(e), e)


# ### Main Program ### #


with FMC(host=host, username=username, password=password, autodeploy=autodeploy) as fmc1:
    logging.info('# ### Mega Test Start!!! ### #')
    starttime = str(int(time.time()))
    namer = '_fmcapi_test_{}'.format(starttime)
    pp = pprint.PrettyPrinter(indent=4)

    test__fmc_version()
    test__url_category()
    test__ports()
    test__application_type()
    test__application_tag()
    test__application()
    test__application_risk()
    test__application_productivity()
    test__application_category()
    test__country()
    test__continent()
    test__vlan_group_tag()
    test__url_group()
    test__network_group()
    test__ip_addresses()
    test__variable_set()
    test__ip_host()
    test__ip_network()
    test__ip_range()
    test__url()
    test__vlan_tag()
    test__protocol_port()
    test__slamonitor()
    test__security_zone()    
    test__device()
    test__intrusion_policy()
    test__access_control_policy()
    test__acp_rule()
    test__audit()
    test__port_object_group()    
    test__intrusion_policy()
    test__access_control_policy()
    test__acp_rule()
    test__audit()
    test__autonat()
    '''
    These tests require registered devices
    #test__device_with_task()
    #test__phys_interfaces()
    #test__device_ha_pair()
    #test__device_ha_monitored_interfaces()
    #test__device_ha_failover_mac()
    #test__interface_group()
    '''