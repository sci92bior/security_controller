package pl.edu.wat.softanet.client

import org.springframework.cloud.openfeign.FeignClient
import org.springframework.stereotype.Component
import org.springframework.web.bind.annotation.GetMapping
import pl.edu.wat.softanet.dto.DeviceDto

@Component
@FeignClient(name = "onosClient", url = "http://localhost:8500/onos/v1/")
interface OnosClient {

    @GetMapping("/devices")
    fun getDevices() : List<DeviceDto>

}