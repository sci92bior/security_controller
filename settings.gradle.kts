rootProject.name = "security_controller"
include(
    "dependencies",
    ":modules:flow_collector",
    ":modules:flow_monitor",
    ":modules:traffic_analyzer",
    ":modules:policy_resolver",
    ":modules:knowlagebase_manager",
    ":modules:device_manager",
    ":modules:flow_pusher",
    ":modules:core"
)
