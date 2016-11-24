

def test_R3_ping_ISP1_GW(dev):
    res = dev.rpc.ping(count="5", rapid=True, host="10.10.0.1")
    # We allow 1 of 5 packets to be lost in this test
    return int(res.findtext("probe-results-summary/packet-loss")) <= 1


def test_R3_ping_ISP2_GW(dev):
    res = dev.rpc.ping(count="5", rapid=True, host="10.20.0.1")
    # We allow 1 of 5 packets to be lost in this test
    return int(res.findtext("probe-results-summary/packet-loss")) <= 1
