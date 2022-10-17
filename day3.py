import batinfo
bat = batinfo.Batteries()
print(bat.stat)
# In [3]: bat
# Out[3]: <batinfo.Battery.Batteries at 0x31c87d0>
# In [4]: bat.stat
# Out[4]: [{"status": "Full", "capacity": 50, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}]
# In [6]: bat.stat[0]
# Out[6]: {"status": "Full", "capacity": 100, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}
# In [7]: bat.stat[0].capacity
# Out[7]: 50
# In [8]: print bat.stat[0]
# 100
# In [9]: bat.stat[0].manufacturer
# Out[9]: 'Fujitsu'
# In [9]: bat.stat[0].technology
# Out[9]: 'Li-ion'
# In [11]: bat.stat[0].charge_full
# Out[11]: 5800000
# In [12]: bat.stat[0].charge_now
# Out[12]: 3900000
# In [12]: bat.update()
# > Refresh the stats


# l1 = [1,2,3,4,5,6,7,8,9,10]
# new_l1 =[]
# while l1:
#     print(l1)
#     l1 = l1 - 1

# str1 = "abcd"
# rev_str = []
# i = 0
# for name in str1:
#     rev_str = i + name
#     print(rev_str)
#product of list
# list1 = [1,2,3,4,5,6,7,8]
# num1 = 1
# for num in list1:
#     num1 = num1 * num
#     print(num1)

#sum of list
# list1 = [1,2,3,4,5,6,7,8]
# num1 = 0
# for num in list1:
#     num1 = num1 + num # num1+=num
#     print(num1)


#odd and even
# list1 = [1,2,3,4,5,6,7,8]
# for num in list1:
#     if num%2==0:
#         print("even:",num)
#     else:
#         print("odd :",num)



# num = 2
# if num >=0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive")
# else:
#     print("Negative")