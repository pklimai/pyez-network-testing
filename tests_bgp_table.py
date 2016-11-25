from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

bgpYAML = """
---
BgpSummaryTable:
  rpc: get-bgp-summary-information
  item: bgp-peer
  key: peer-address
  view: BgpSummaryView

BgpSummaryView:
  fields:
    peer_ip: peer-address
    peer_as: peer-as
    peer_state: peer-state
"""

def test_R2_bgp_peers_established(dev):
    globals().update(FactoryLoader().load(yaml.load(bgpYAML)))
    bgp_table = BgpSummaryTable(dev).get()
    for peer in bgp_table:
        if peer["peer_state"] != "Established":
            return False
    return True
