package pl.edu.wat.softanet.handler

import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.ControllerAdvice
import org.springframework.web.bind.annotation.ExceptionHandler
import pl.edu.wat.softanet.exception.OnosClientException


@ControllerAdvice
class DeviceHandler {

    @ExceptionHandler(OnosClientException::class)
    fun handleAISearcherObjectNotFoundException(ex: OnosClientException): ResponseEntity<String> {
        return ResponseEntity(ex.message, HttpStatus.NOT_FOUND)
    }
}