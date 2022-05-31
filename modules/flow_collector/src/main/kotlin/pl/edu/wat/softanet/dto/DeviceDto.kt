package pl.edu.wat.softanet.dto

data class Devices(
    val devices : List<DeviceDto>? = null
)
data class DeviceDto(
    val annotations: Annotations?= null,
    val available: Boolean?= null,
    val chassisId: String?= null,
    val driver: String?= null,
    val humanReadableLastUpdate: String?= null,
    val hw: String?= null,
    val id: String?= null,
    val lastUpdate: String?= null,
    val mfr: String?= null,
    val role: String?= null,
    val serial: String?= null,
    val sw: String?= null,
    val type: String?= null,
)