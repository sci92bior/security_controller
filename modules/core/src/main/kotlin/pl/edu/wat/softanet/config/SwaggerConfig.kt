package pl.edu.wat.softanet.config

import org.springframework.beans.factory.annotation.Value
import org.springframework.boot.info.BuildProperties
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.context.annotation.Import
import org.springframework.http.HttpHeaders
import springfox.bean.validators.configuration.BeanValidatorPluginsConfiguration
import springfox.documentation.builders.ApiInfoBuilder
import springfox.documentation.builders.PathSelectors
import springfox.documentation.builders.RequestHandlerSelectors
import springfox.documentation.service.ApiKey
import springfox.documentation.service.SecurityScheme
import springfox.documentation.spi.DocumentationType
import springfox.documentation.spring.web.plugins.Docket


const val JWT_TOKEN_API_KEY_NAME = "JWT Token"

@Configuration
@Import(BeanValidatorPluginsConfiguration::class)
internal class SwaggerConfig(
        private val buildProperties: BuildProperties
) {

    @Value("\${git.commit.id}")
    private val commitId: String? = null

    @Value("\${git.branch}")
    private val branch: String? = null

    @Bean
    fun api(): Docket = Docket(DocumentationType.SWAGGER_2)
            .select()
            .apis(RequestHandlerSelectors.basePackage("pl.edu.wat.softanet.controller"))
            .paths(PathSelectors.any())
            .build()
            .apiInfo(
                    ApiInfoBuilder()
                            .title("Security Controller API")
                            .version("   Version: ${buildProperties.version}\n    Branch: $branch\n    Commit: $commitId ")
                            .build()
            )
            .securitySchemes(listOf(ApiKey(JWT_TOKEN_API_KEY_NAME, HttpHeaders.AUTHORIZATION, "header")) as List<SecurityScheme>)


}
