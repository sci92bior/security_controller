object Versions {
    const val springBoot = "2.5.6"
    const val kotlin = "1.5.31"
    const val postgresql = "42.3.0"
    const val kLogging = "2.0.11"
    const val jacksonModuleKotlin = "2.13.0"
    const val javaxValidation = "2.0.1.Final"
    const val hibernateValidator = "6.1.0.Final"
    const val swagger = "3.0.0"
    const val junit5 = "5.8.1"
    const val springMockk = "3.0.1"
    const val liquibaseCore = "4.5.0"
    const val logbackCore = "1.2.3"
    const val liquibasePlugin = "2.0.4"
    const val minio = "8.3.3"
    const val okHttp3 = "4.9.2"
    const val keycloak = "15.0.2"
    const val keycloakMock = "2.4.0" // TODO 3.0.4
    const val commonsCsv = "1.9.0"
    const val zxing = "3.4.1"
}

object Dependency {
    const val springBootStarter = "org.springframework.boot:spring-boot-starter-web:${Versions.springBoot}"
    const val springBootDependencies = "org.springframework.boot:spring-boot-dependencies:${Versions.springBoot}"
    const val springCloudFeign = "org.springframework.cloud:spring-cloud-starter-openfeign:3.0.3"

    const val springBootStarterDataAop = "org.springframework.boot:spring-boot-starter-aop"
    const val springBootStarterDataJpa = "org.springframework.boot:spring-boot-starter-data-jpa"
    const val springBootStarterActuator = "org.springframework.boot:spring-boot-starter-actuator"
    const val springBootSecurity = "org.springframework.boot:spring-boot-starter-security"

    const val springBootStarterTest = "org.springframework.boot:spring-boot-starter-test"

    const val postgresql = "org.postgresql:postgresql:${Versions.postgresql}"
    const val h2 = "com.h2database:h2"
    const val javaxValidation = "javax.validation:validation-api:${Versions.javaxValidation}"
    const val hibernateValidator = "org.hibernate.validator:hibernate-validator:${Versions.hibernateValidator}"

    const val kotlinReflect = "org.jetbrains.kotlin:kotlin-reflect:${Versions.kotlin}"
    const val kotlinJkd8 = "org.jetbrains.kotlin:kotlin-stdlib-jdk8:${Versions.kotlin}"
    const val kLogging = "io.github.microutils:kotlin-logging-jvm:${Versions.kLogging}"
    const val jacksonModuleKotlin = "com.fasterxml.jackson.module:jackson-module-kotlin:${Versions.jacksonModuleKotlin}"

    const val liquibaseCore = "org.liquibase:liquibase-core:${Versions.liquibaseCore}"
    const val logbackCore = "ch.qos.logback:logback-core:${Versions.logbackCore}"
    const val logbackClassic = "ch.qos.logback:logback-classic:${Versions.logbackCore}"

    const val swagger = "io.springfox:springfox-boot-starter:${Versions.swagger}"
    const val swaggerValidators = "io.springfox:springfox-bean-validators:${Versions.swagger}"

    const val junit5 = "org.junit.jupiter:junit-jupiter:${Versions.junit5}"
    const val junitApi = "org.junit.jupiter:junit-jupiter-api:${Versions.junit5}"
    const val springMockk = "com.ninja-squad:springmockk:${Versions.springMockk}"

    const val minio = "io.minio:minio:${Versions.minio}"
    const val okHttp3 = "com.squareup.okhttp3:okhttp:${Versions.okHttp3}"

    const val keycloak = "org.keycloak:keycloak-spring-boot-starter:${Versions.keycloak}"
    const val keycloakAdapter = "org.keycloak.bom:keycloak-adapter-bom:${Versions.keycloak}"
    const val keycloakAdminClient = "org.keycloak:keycloak-admin-client:${Versions.keycloak}"
    const val keycloakMock =
        "com.c4-soft.springaddons:spring-security-oauth2-test-webmvc-addons:${Versions.keycloakMock}"

    const val commonsCsv = "org.apache.commons:commons-csv:${Versions.commonsCsv}"
    const val zxingCore = "com.google.zxing:core:${Versions.zxing}"
    const val zxingJse = "com.google.zxing:javase:${Versions.zxing}"
}

object Plugins {
    const val jvm = "jvm"
    const val kapt = "kapt"
    const val jpa = "org.jetbrains.kotlin.plugin.jpa"
    const val noArg = "org.jetbrains.kotlin.plugin.noarg"
    const val springBoot = "org.springframework.boot"
    const val kotlinSpring = "org.jetbrains.kotlin.plugin.spring"
    const val springDependencyManagement = "io.spring.dependency-management"
    const val liquibase = "org.liquibase.gradle"
    const val gitCommitPlugin = "com.gorylenko.gradle-git-properties"
}
