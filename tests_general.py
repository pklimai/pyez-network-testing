

def test_all_chassis_alarms(dev):
    rpc_result = dev.rpc.get_alarm_information()
    return rpc_result.find("alarm-summary/no-active-alarms") is not None


def test_all_system_alarms(dev):
    rpc_result = dev.rpc.get_system_alarm_information()
    return rpc_result.find("alarm-summary/no-active-alarms") is not None


def test_all_core_dumps(dev):
    rpc_result = dev.rpc.get_system_core_dumps()
    return rpc_result.find("directory/file-information") is None