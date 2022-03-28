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
    implementation(Dependency.springBootStarter)
    implementation(Dependency.springBootStarterDataJpa)
    implementation(Dependency.springBootStarterDataAop)
    implementation(Dependency.springBootStarterActuator)
    implementation(Dependency.kotlinJkd8)
    implementation(Dependency.kotlinReflect)

    implementation(Dependency.swagger)
    implementation(Dependency.swaggerValidators)

}
