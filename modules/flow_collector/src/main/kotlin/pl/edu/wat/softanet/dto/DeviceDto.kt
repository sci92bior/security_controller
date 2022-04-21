package pl.edu.wat.softanet.dto

data class DeviceDto (
    val type: DeviceType?,
    val manufacturer: String?,
    val hwVersion: String?,
    val swVersion: String?,
    val serialNumber: String?
)