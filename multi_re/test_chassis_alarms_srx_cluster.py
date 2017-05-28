
def test_all_chassis_alarms(dev):
    rpc_result = dev.rpc.get_alarm_information()

    if rpc_result.find("multi-routing-engine-item") is not None:
        re_with_no_alarms = 0
        multi_re_alarms = rpc_result.xpath("multi-routing-engine-item/alarm-information/*")
        for alarm_inf in multi_re_alarms:
            if alarm_inf.find("no-active-alarms") is not None:
                re_with_no_alarms += 1
        return re_with_no_alarms == 2
    
    else:
        return rpc_result.find("alarm-summary/no-active-alarms") is not None
