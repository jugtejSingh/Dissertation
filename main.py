import math
import random

import pandas as pd
import traci
from matplotlib import pyplot as plt
import Data
import Randomizer


def realTimeFlow():
    carStep = 0

    eastBoundTime = 0
    westBoundTime = 0
    southBoundTime = 0
    northBoundTime = 0

    eastBoundTimeSpace = 0
    westBoundTimeSpace = 0
    northBoundTimeSpace = 0
    southBoundTimeSpace = 0

    eastBoundList = []
    westBoundList = []
    northBoundList = []
    southBoundList = []

    list_of_current_cars = []
    vehicles = []
    arrived_vehicles = []
    waiting_time_list = []
    # 53200 is chosen due to a problem with sumo, Original value is 53100
    for step in range(86500):
        #Traffic Algorithms
        fixed_timer(step,10,10)
        # new_induction_loops(step)
        # detector_rezgui()
        # randomised_fixed_timer(step).
        if step % 900 == 0:
            carStep = math.floor(step / 900)
            if carStep == 96:
                carStep = 95
            eastBoundTime = 0
            westBoundTime = 0
            southBoundTime = 0
            northBoundTime = 0

            # Gets the vehicle could for that interval
            eastBound = Data.eastCount[carStep]
            westBound = Data.westCount[carStep]
            northBound = Data.northCount[carStep]
            southBound = Data.southCount[carStep]
            # Diving the number by interval gives the time delay that is needed before adding the vehicles so we can have
            # the exact number of vehicles
            if eastBound == 0:
                eastBound = 1
            if westBound == 0:
                westBound = 1
            if northBound == 0:
                northBound = 1
            if southBound == 0:
                southBound = 1
            eastBoundTimeSpace = math.floor(900 / eastBound)
            westBoundTimeSpace = math.floor(900 / westBound)
            northBoundTimeSpace = math.floor(900 / northBound)
            southBoundTimeSpace = math.floor(900 / southBound)

        eastBoundTime += 1
        westBoundTime += 1
        northBoundTime += 1
        southBoundTime += 1
        # This checks if that interval has been met, If it has then it means that a new vehicle can be added and the time
        # goes back to 0
        if eastBoundTime == eastBoundTimeSpace:
            randomizer1 = Randomizer.randomForTravisLeft()
            traci.vehicle.add(f"vehicle_{step}_east", RouteCreation.travisRightEntrytList[randomizer1])
            eastBoundTime = 0

        if westBoundTime == westBoundTimeSpace:
            randomizer2 = Randomizer.randomForTravisRight()
            traci.vehicle.add(f"vehicle_{step}_west", RouteCreation.travisLeftEntrytList[randomizer2])
            westBoundTime = 0

        if northBoundTime == northBoundTimeSpace:
            randomizer3 = Randomizer.randomForKellyUp()
            traci.vehicle.add(f"vehicle_{step}_north", RouteCreation.kellyUpEntryList[randomizer3])
            northBoundTime = 0

        if southBoundTime == southBoundTimeSpace:
            randomizer4 = Randomizer.randomForKellyDown()
            traci.vehicle.add(f"vehicle_{step}_south", RouteCreation.kellyDownEntryList[randomizer4])
            southBoundTime = 0
        # At every interval i.
        # t gets the value from the induction loops about the number of vehicles on top of it
        if step % 900 == 0:
            if step == 0:
                print("Starting simulation")
            else:
                KellyUpLoop = traci.inductionloop.getLastIntervalVehicleNumber("KellyUpLoop")
                TravisLeftLoop = traci.inductionloop.getLastIntervalVehicleNumber("TravisLeftLoop")
                KellyDownLoop = traci.inductionloop.getLastIntervalVehicleNumber("KellyDownLoop")
                TravisRightLoop = traci.inductionloop.getLastIntervalVehicleNumber("TravisRightLoop")
                # Adds them to a list
                eastBoundList.append(TravisRightLoop)
                westBoundList.append(TravisLeftLoop)
                northBoundList.append(KellyUpLoop)
                southBoundList.append(KellyDownLoop)

        vehicles = waitingTime(list_of_current_cars, arrived_vehicles, vehicles)
        traci.simulationStep()
    traci.close()
    for value in vehicles:
        for x in value.values():
            waiting_time_list.append(max(x))
    print(sum(waiting_time_list) / len(waiting_time_list))
    return eastBoundList, westBoundList, northBoundList, southBoundList


def randomized_flow():
    list_of_current_cars = []
    vehicles = []
    arrived_vehicles = []
    waiting_time_list = []
    directionRoutes = [RouteCreation.travisRightEntrytList, RouteCreation.travisLeftEntrytList,
                       RouteCreation.kellyUpEntryList, RouteCreation.kellyDownEntryList]
    random_interval = 0
    for step in range(43200):
        #Traggic Algorithms
        # fixed_timer(step,10,10)
        # new_induction_loops(step)
        # detector_rezgui()
        # randomised_fixed_timer(step)
        random_direction = random.randint(0, 3)
        random_route = random.randint(0, 3)
        randomizer_checker = random.randint(1, 20)
        if randomizer_checker == 20:
            random_interval = 0
        if random_interval == 0:
            traci.vehicle.add(f"vehicle_{step}_east", directionRoutes[random_direction][random_route])
            random_interval = random.randint(1, 10)
        else:
            random_interval = random_interval - 1
        vehicles = waitingTime(list_of_current_cars, arrived_vehicles, vehicles)
        traci.simulationStep()
    traci.close()
    for value in vehicles:
        for x in value.values():
            waiting_time_list.append(max(x))
    print(sum(waiting_time_list) / len(waiting_time_list))


def randomized_horde_flow():
    list_of_current_cars = []
    vehicles = []
    arrived_vehicles = []
    waiting_time_list = []
    directionRoutes = [RouteCreation.travisRightEntrytList, RouteCreation.travisLeftEntrytList,
                       RouteCreation.kellyUpEntryList, RouteCreation.kellyDownEntryList]
    random_interval = 0
    for step in range(43200):
        # Traffic Algorithms
        # fixed_timer(step,10,10)
        # new_induction_loops(step)
        # detector_rezgui()
        # randomised_fixed_timer(step)
        random_direction = random.randint(0, 3)
        random_route = random.randint(0, 3)
        random_number_of_cars = random.randint(1, 15)
        if random_interval == 0:
            for x in range(random_number_of_cars):
                traci.vehicle.add(f"vehicle_{step}_horde" + str(x), directionRoutes[random_direction][random_route])
            random_interval = random.randint(1, 25)
        else:
            random_interval = random_interval - 1
        vehicles = waitingTime(list_of_current_cars, arrived_vehicles, vehicles)
        traci.simulationStep()
    traci.close()
    for value in vehicles:
        for x in value.values():
            waiting_time_list.append(max(x))
    print(sum(waiting_time_list) / len(waiting_time_list))


def equalized_flow():
    list_of_current_cars = []
    vehicles = []
    arrived_vehicles = []
    waiting_time_list = []
    directionRoutes = [RouteCreation.travisRightEntrytList, RouteCreation.travisLeftEntrytList,
                       RouteCreation.kellyUpEntryList, RouteCreation.kellyDownEntryList]
    random_interval = 0

    for step in range(43200):
        # traffic light code
        # fixed_timer(step,10,10)
        # new_induction_loops(step)
        # detector_rezgui()
        # randomised_fixed_timer(step)
        # flow code
        if random_interval == 0:
            for x in range(4):
                random_route = random.randint(0, 3)
                traci.vehicle.add(f"vehicle_{step}_" + str(x), directionRoutes[x][random_route])
            random_interval = 15
        else:
            random_interval = random_interval - 1
        # waiting time code
        vehicles = waitingTime(list_of_current_cars, arrived_vehicles, vehicles)
        traci.simulationStep()
    traci.close()
    for value in vehicles:
        for x in value.values():
            waiting_time_list.append(max(x))
    print(sum(waiting_time_list) / len(waiting_time_list))


# Uses the same time for all as they are all using the same time, This function just plots everything


def fixed_timer(step, green, second_green):
    traffic_light_id = "42960195"
    starter = step % (green + second_green + 3 + 4)
    if starter <= green:
        # traffic light codes are north east south west
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "ggggrrrrggggrrrr")
    elif green + 1 <= starter <= green + 3:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "yyyyuuuuyyyyuuuu")
    elif green + 5 <= starter <= green + second_green + 3:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "rrrrggggrrrrgggg")
    else:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "uuuuyyyyuuuuyyyy")




lock = 0
# The code has an issue of when it goes into starter == 0, It doesnt actually update the starter value and causes a problem with the traffic light system
def randomised_fixed_timer(step):
    traffic_light_id = "42960195"
    global lock, constant_h_randomizer, constant_v_randomizer, starter
    constant_h = 10
    constant_v = 10
    if lock == 0:
        randomized_timer_v = random.uniform(0.5, 1.5)
        randomized_timer_h = random.uniform(0.5, 1.5)
        constant_h_randomizer = (math.floor(constant_h * randomized_timer_h))
        constant_v_randomizer = (math.floor(constant_v * randomized_timer_v))
        starter = 1
        lock = 1
    if starter <= constant_h_randomizer:
        # traffic light codes are north east south west
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "ggggrrrrggggrrrr")
    elif constant_h_randomizer + 1 <= starter <= constant_h_randomizer + 3:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "yyyyuuuuyyyyuuuu")
    elif constant_h_randomizer + 4 <= starter <= constant_h_randomizer + constant_v_randomizer + 3:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "rrrrggggrrrrgggg")
    elif constant_h_randomizer + constant_v_randomizer + 4 <= starter <= constant_h_randomizer + constant_v_randomizer + 5:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "uuuuyyyyuuuuyyyy")
    else:
        traci.trafficlight.setRedYellowGreenState(traffic_light_id, "uuuuyyyyuuuuyyyy")
        lock = 0
    starter = starter + 1

time_lock_for_loops = 10000000


def new_induction_loops(step):
    global time_lock_for_loops
    traffic_light_id = "42960195"
    if step == 1:
        traci.trafficlight.setProgram(traffic_light_id, 0)

    if traci.trafficlight.getPhase(traffic_light_id) == 2:
        if traci.trafficlight.getNextSwitch(traffic_light_id) - traci.simulation.getTime() == 0:
            if traci.inductionloop.getLastStepOccupancy(
                    "KellyUpLoop2") >= 80 or traci.inductionloop.getLastStepOccupancy("KellyDownLoop2") >= 80:
                traci.trafficlight.setProgram(traffic_light_id, 1)
                traci.trafficlight.setPhase(traffic_light_id, 3)
                time_lock_for_loops = traci.simulation.getTime() + 18
                print("Inside Kelly Loop1" + str(traci.simulation.getTime()))
                if traci.inductionloop.getLastStepOccupancy(
                        "KellyUpLoop3") >= 80 or traci.inductionloop.getLastStepOccupancy("KellyDownLoop3") >= 80:
                    traci.trafficlight.setProgram(traffic_light_id, 3)
                    traci.trafficlight.setPhase(traffic_light_id, 3)
                    time_lock_for_loops = traci.simulation.getTime() + 23
                    print("Inside Kelly Loop2" + str(traci.simulation.getTime()))
            else:
                if time_lock_for_loops == traci.simulation.getTime():
                    traci.trafficlight.setProgram(traffic_light_id, 0)
                    traci.trafficlight.setPhase(traffic_light_id, 3)

    elif traci.trafficlight.getPhase(traffic_light_id) == 0:
        if traci.inductionloop.getLastStepOccupancy(
                "TravisLeftLoop2") >= 80 or traci.inductionloop.getLastStepOccupancy("TravisRightLoop2") >= 80:
            traci.trafficlight.setProgram(traffic_light_id, 1)
            traci.trafficlight.setPhase(traffic_light_id, 1)
            traci.simulation.getTime() + 18
            if traci.inductionloop.getLastStepOccupancy(
                    "TravisLeftLoop2") >= 80 or traci.inductionloop.getLastStepOccupancy("TravisRightLoop2") >= 80:
                traci.trafficlight.setProgram(traffic_light_id, 3)
                traci.trafficlight.setPhase(traffic_light_id, 1)
                traci.simulation.getTime() + 23
        else:
            if time_lock_for_loops == traci.simulation.getTime():
                traci.trafficlight.setProgram(traffic_light_id, 0)
                traci.trafficlight.setPhase(traffic_light_id, 1)


# find a way to add both horizontal + vertical to ensure most of the area is being looked aftera
# Fix phases for the light

time_lock_for_detectors = 0


def detector_rezgui():
    global time_lock_for_detectors
    traffic_light_id = "42960195"
    horizontal_way = traci.lanearea.getJamLengthVehicle("KellyUpDetector") + traci.lanearea.getJamLengthVehicle(
        "KellyDownDetector")
    vertical_way = traci.lanearea.getJamLengthVehicle("TravisLeftDetector") + traci.lanearea.getJamLengthVehicle(
        "TravisRightDetector")
    if traci.simulation.getTime() >= time_lock_for_detectors:
        print("Entered")
        if horizontal_way >= vertical_way:
            if traci.trafficlight.getPhase(traffic_light_id) == 2:
                print("Phase 3")
                traci.trafficlight.setProgram(traffic_light_id, 0)
                traci.trafficlight.setPhase(traffic_light_id, 3)
                time_lock_for_detectors = traci.simulation.getTime() + 8
        else:
            if traci.trafficlight.getPhase(traffic_light_id) == 0:
                print("Phase 1")
                traci.trafficlight.setProgram(traffic_light_id, 0)
                traci.trafficlight.setPhase(traffic_light_id, 1)
                time_lock_for_detectors = traci.simulation.getTime() + 8

def waitingTime(list_of_current_cars, arrived_vehicles, vehicles):
    if len(traci.simulation.getDepartedIDList()) > 0:
        for id in traci.simulation.getDepartedIDList():
            list_of_current_cars.append(id)
    for vehID in list_of_current_cars:

        for x in traci.simulation.getArrivedIDList():
            arrived_vehicles.append(x)

        if vehID in arrived_vehicles:
            list_of_current_cars.remove(vehID)
            continue
        else:
            vehicle_keys = []
            for keys in vehicles:
                for key in keys.keys():
                    vehicle_keys.append(key)

            if vehID not in vehicle_keys:
                vehicles.append({vehID: []})

            for vehicle_data in vehicles:  # Loop through vehicles dictionary
                if vehID in vehicle_data.keys():
                    waiting_time = traci.vehicle.getWaitingTime(vehID)
                    vehicle_data[vehID].append(waiting_time)
    return vehicles


def plotForRealTimeDataFlow(RealTimedirection, OriginalDirection, DirectionForChart):
    time = Data.easttime
    vehCount = RealTimedirection

    df = pd.DataFrame({"Original": OriginalDirection, "Simulated": RealTimedirection})
    df["Difference"] = abs(df["Original"] - df["Simulated"])
    print(f"Standard Deviation of {DirectionForChart}" + str(df["Difference"].std()))

    fig = plt.figure(figsize=(30, 8))
    ax1 = fig.add_subplot(111)

    ax1.plot(time, vehCount, label="Recreation")
    ax1.plot(time, OriginalDirection, label="Original")
    ax1.set_ylabel("Vehicular Count")
    ax1.set_xlabel("Time")
    plt.legend(["Simulated", "Original"])
    ax1.set_title(f"{DirectionForChart} Charts using Sumo")
    plt.savefig(f"{DirectionForChart} using sumo.png")
    plt.show()



traci.start(["sumo-gui", "-c", "C:/Users/jugte/Sumo/2024-02-06-06-31-46/osm.sumocfg"])
import RouteCreation

#Please uncomment one of these and comment the rest to run a type of flow. In the functions for each flow which can be
# You can find the functions for each of the algorithms. Comment one and uncomment the rest of the traffic algorithms in
# to run that specific one. You can swap the data used by the real data algorithm by going to the
#Data.py and changing out which file is used.
eastBoundList, westBoundList, northBoundList, southBoundList = realTimeFlow()
# randomized_flow()
# randomized_horde_flow()
# equalized_flow()

plotForRealTimeDataFlow(eastBoundList, Data.eastCount, "EastBound")
plotForRealTimeDataFlow(westBoundList, Data.westCount, "WestBound")
plotForRealTimeDataFlow(northBoundList, Data.northCount, "NorthBound")
plotForRealTimeDataFlow(southBoundList, Data.southCount, "SouthBound")
