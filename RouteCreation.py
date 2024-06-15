import traci

traci.route.add("kellyDownEntry_kellyDownExit", ("KellyDownEntry", "KellyDownExit"))
traci.route.add("kellyDownEntry_travisLeftExit", ("KellyDownEntry", "TravisLeftExit"))
traci.route.add("kellyDownEntry_kellyUpExit", ("KellyDownEntry", "KellyUpExit"))
traci.route.add("kellyDownEntry_travisRightExit", ("KellyDownEntry", "TravisRightExit"))

kellyDownEntry1 = "kellyDownEntry_kellyDownExit"
kellyDownEntry2 = "kellyDownEntry_travisLeftExit"
kellyDownEntry3 = "kellyDownEntry_kellyUpExit"
kellyDownEntry4 = "kellyDownEntry_travisRightExit"

kellyDownEntryList = [kellyDownEntry1, kellyDownEntry2, kellyDownEntry3, kellyDownEntry4]

traci.route.add("travisLeftEntry_kellyDownExit", ("TravisLeftEntry", "KellyDownExit"))
traci.route.add("travisLeftEntry_travisLeftExit", ("TravisLeftEntry", "TravisLeftExit"))
traci.route.add("travisLeftEntry_kellyUpExit", ("TravisLeftEntry", "KellyUpExit"))
traci.route.add("travisLeftEntry_travisRightExit", ("TravisLeftEntry", "TravisRightExit"))

travisLeftEntry1 = "travisLeftEntry_kellyDownExit"
travisLeftEntry2 = "travisLeftEntry_travisLeftExit"
travisLeftEntry3 = "travisLeftEntry_kellyUpExit"
travisLeftEntry4 = "travisLeftEntry_travisRightExit"
travisLeftEntrytList = [travisLeftEntry1, travisLeftEntry2, travisLeftEntry3, travisLeftEntry4]

traci.route.add("travisRightEntry_kellyDownExit", ("TravisRightEntry", "KellyDownExit"))
traci.route.add("travisRightEntry_travisLeftExit", ("TravisRightEntry", "TravisLeftExit"))
traci.route.add("travisRightEntry_kellyUpExit", ("TravisRightEntry", "KellyUpExit"))
traci.route.add("travisRightEntry_travisRightExit", ("TravisRightEntry", "TravisRightExit"))

travisRightEntry1 = "travisRightEntry_kellyDownExit"
travisRightEntry2 = "travisRightEntry_travisLeftExit"
travisRightEntry3 = "travisRightEntry_kellyUpExit"
travisRightEntry4 = "travisRightEntry_travisRightExit"

travisRightEntrytList = [travisRightEntry1, travisRightEntry2, travisRightEntry3, travisRightEntry4]

traci.route.add("kellyUpEntry_kellyDownExit", ("KellyUpEntry", "KellyDownExit"))
traci.route.add("kellyUpEntry_travisLeftExit", ("KellyUpEntry", "TravisLeftExit"))
traci.route.add("kellyUpEntry_kellyUpExit", ("KellyUpEntry", "KellyUpExit"))
traci.route.add("kellyUpEntry_travisRightExit", ("KellyUpEntry", "TravisRightExit"))

kellyUpEntry1 = "kellyUpEntry_kellyDownExit"
kellyUpEntry2 = "kellyUpEntry_travisLeftExit"
kellyUpEntry3 = "kellyUpEntry_kellyUpExit"
kellyUpEntry4 = "kellyUpEntry_travisRightExit"

kellyUpEntryList = [kellyUpEntry1, kellyUpEntry2, kellyUpEntry3, kellyUpEntry4]
