import jxmlease

def test_all_total_memory_percent_util(dev):
    parser = jxmlease.EtreeParser()
    res = parser(dev.rpc.get_route_engine_information())
    # The 80% threshold is arbitrary and you might want to set different number in your env.
    # Also consider checking control and data plane memory utilization separately
    return int(res["route-engine-information"]["route-engine"]["memory-system-total-util"]) < 80
