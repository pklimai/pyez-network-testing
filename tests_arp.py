import jxmlease


def test_R1_arp_gateway(dev):
    R1_GW_CORRECT_ARP_ENTRY = {
        'arp-table-entry-flags': {'none': ''},
        'hostname': '10.10.0.1',
        'interface-name': 'ge-0/0/3.0',
        'ip-address': '10.10.0.1',
        'mac-address': '00:0c:29:60:25:80'
    }
    parser = jxmlease.EtreeParser()
    res = parser(dev.rpc.get_arp_table_information())
    # You can use res.prettyprint() to see the whole data structure
    for item in res['arp-table-information']['arp-table-entry']:
        if item == R1_GW_CORRECT_ARP_ENTRY:
            return True
    return False


def test_R2_arp_gateway(dev):
    R2_GW_CORRECT_ARP_ENTRY = {
        'arp-table-entry-flags': {'none': ''},
        'hostname': '10.20.0.1',
        'interface-name': 'ge-0/0/3.0',
        'ip-address': '10.20.0.1',
        'mac-address': '00:0c:29:60:25:8a'
    }
    parser = jxmlease.EtreeParser()
    res = parser(dev.rpc.get_arp_table_information())
    # You can use res.prettyprint() to see the whole data structure
    for item in res['arp-table-information']['arp-table-entry']:
        if item == R2_GW_CORRECT_ARP_ENTRY:
            return True
    return False
