from jnpr.junos.op.ospf import OspfNeighborTable


def check_ospf_full_adjacencies(dev, neighbor_count):
    ospf_table = OspfNeighborTable(dev)    # Create an instance of the Table
    ospf_table.get()                       # Populate the Table
    if len(ospf_table) != neighbor_count:
        return False
    for neighbor in ospf_table:
        if neighbor["ospf_neighbor_state"] != "Full":
            return False
    return True


def test_R1_ospf(dev):
    return check_ospf_full_adjacencies(dev, 3)


def test_R2_ospf(dev):
    return check_ospf_full_adjacencies(dev, 3)


def test_R3_ospf(dev):
    return check_ospf_full_adjacencies(dev, 2)
