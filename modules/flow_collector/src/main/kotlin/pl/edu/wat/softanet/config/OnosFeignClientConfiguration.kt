package pl.edu.wat.softanet.config

import feign.auth.BasicAuthRequestInterceptor
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration


@Configuration
class OnosFeignClientConfiguration {
    @Bean
    fun basicAuthRequestInterceptor(): BasicAuthRequestInterceptor {
        return BasicAuthRequestInterceptor("onos", "rocks")
    }
}