package pl.edu.wat.softanet.controller

import io.swagger.annotations.*
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import pl.edu.wat.softanet.dto.DeviceDto
import pl.edu.wat.softanet.facade.DeviceFacade

const val DEVICE_BASE_URL = "/api/device"

@RestController
@RequestMapping(DEVICE_BASE_URL)
@Api(value = "Device", tags = ["device"])
class DeviceController(private val deviceFacade: DeviceFacade) {

    @ApiOperation(value = "Get devices", nickname = "getDevices", response = List::class, tags = ["device"])
    @ApiResponses(value = [ApiResponse(code = 200, message = "Successful operation", response = List::class)])
    @GetMapping(value = ["/"], produces = ["application/json"])
    fun getDevices(): ResponseEntity<List<DeviceDto>> {
        val devices = deviceFacade.getAllDevicesConnected()
        return ResponseEntity.ok(devices)
    }
}