

def test_R3_bgp_default(dev):
    rpc_result = dev.rpc.get_route_information(protocol="bgp", destination="0.0.0.0/0", exact=True)
    nh_list = []
    for item in rpc_result.findall("route-table[table-name='inet.0']/rt[rt-destination='0.0.0.0/0']/rt-entry/nh/to"):
        nh_list.append(item.findtext("."))
    nh_list.sort()
    return nh_list == ["10.3.0.1", "10.4.0.1"]


def test_R1_bgp_default(dev):
    rpc_result = dev.rpc.get_route_information(protocol="bgp", destination="0.0.0.0/0", exact=True)
    nh_list = []
    for item in rpc_result.findall("route-table[table-name='inet.0']/rt[rt-destination='0.0.0.0/0']/rt-entry/nh/to"):
        nh_list.append(item.findtext("."))
    nh_list.sort()
    return nh_list == ["10.1.0.222", "10.10.0.1", "10.2.0.222"]
