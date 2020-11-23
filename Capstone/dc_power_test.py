from plug34461A import plug34461A
from time import sleep
from datetime import datetime

def dc_power_test():
    """
    Power consumption test using the 34461A DMM
    """

    DUT = input("Please enter the DUT serial number.")
    tester = input("Please enter your name")
    dmm_ip = "TCPIP::192.168.10.52::inst0::INSTR"
    try:
        dmm = plug34461A(dmm_ip)

    except Exception as e:
        print(e)
        print("Could not initialize dmm ... ending test")
        return

    #calculate the power 
    power = dmm.read_current(2) * dmm.read_voltage(2)

    print("DC Power: {} Watts".format(power))

    #writing to a file 
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        fileName = "powertest_{}.txt".format(timestamp)
        f = open(fileName, "w")
        f.write("Test Time: {}\nDUT: {}\n Tester: {}\n Result: {}\n Watts".format(timestamp, DUT, tester, result))
        f.close()
    except Exception as e:
        print(e)
        print("Failed writing results to file.")
        return

    print("Test completed.")
    return


if __name__ == "__main__":
    dc_power_test()