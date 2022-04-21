plugins {
    kotlin(Plugins.jvm)
    kotlin(Plugins.kapt)
    id(Plugins.springBoot)
    id(Plugins.gitCommitPlugin).version("2.3.2")
}

springBoot {
    mainClassName = "pl.edu.wat.softanet.SecurityControllerApplicationKt"
    buildInfo()
}

dependencies {
    implementation(project(":modules:flow_collector"))

    implementation("com.h2database:h2:2.1.212")
    implementation("org.springframework.cloud:spring-cloud-starter-openfeign:3.0.3")
    implementation(Dependency.springBootStarter)
    implementation(Dependency.springBootStarterDataJpa)
    implementation(Dependency.springBootStarterDataAop)
    implementation(Dependency.springBootStarterActuator)
    implementation(Dependency.kotlinJkd8)
    implementation(Dependency.kotlinReflect)

    implementation(Dependency.swagger)
    implementation(Dependency.swaggerValidators)

}
