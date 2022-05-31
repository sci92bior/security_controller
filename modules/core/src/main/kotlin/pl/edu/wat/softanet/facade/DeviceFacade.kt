package pl.edu.wat.softanet.facade

import org.springframework.stereotype.Service
import pl.edu.wat.softanet.client.OnosClient
import pl.edu.wat.softanet.dto.DeviceDto
import pl.edu.wat.softanet.dto.Devices
import pl.edu.wat.softanet.exception.OnosClientException

@Service
class DeviceFacade(private val onosClient: OnosClient) {

    fun getAllDevicesConnected() : Devices{
        try {
            return onosClient.getDevices()
        }catch (e : Exception){
            throw OnosClientException(e.message!!)
        }
    }
}