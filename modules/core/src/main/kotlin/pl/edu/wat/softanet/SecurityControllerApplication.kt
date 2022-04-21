package pl.edu.wat.softanet

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.cloud.openfeign.EnableFeignClients
import springfox.documentation.swagger2.annotations.EnableSwagger2

@EnableFeignClients
@SpringBootApplication
@EnableSwagger2

class SecurityControllerApplication

fun main(args: Array<String>) {
    runApplication<SecurityControllerApplication>(*args)
}