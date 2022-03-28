package pl.edu.wat.softanet

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import springfox.documentation.swagger2.annotations.EnableSwagger2

@SpringBootApplication
@EnableSwagger2
class SecurityControllerApplication

fun main(args: Array<String>) {
    runApplication<SecurityControllerApplication>(*args)
}