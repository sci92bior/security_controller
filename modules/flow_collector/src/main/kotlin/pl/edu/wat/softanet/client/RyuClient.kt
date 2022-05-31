package pl.edu.wat.softanet.client

import org.springframework.cloud.openfeign.FeignClient
import org.springframework.stereotype.Component
import org.springframework.web.bind.annotation.GetMapping
import pl.edu.wat.softanet.config.OnosFeignClientConfiguration
import pl.edu.wat.softanet.dto.Devices

@Component
@FeignClient(name = "onosClient", configuration = [OnosFeignClientConfiguration::class],url = "http://localhost:8181/onos/v1/")
interface RyuClient {

    @GetMapping("/devices")
    fun getDevices() : Devices

}
