import io.spring.gradle.dependencymanagement.dsl.DependencyManagementExtension
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
	base
	kotlin(Plugins.jvm) version Versions.kotlin apply false
	kotlin(Plugins.kapt) version Versions.kotlin apply false
	id(Plugins.jpa) version Versions.kotlin apply false
	id(Plugins.kotlinSpring) version Versions.kotlin apply false
	id(Plugins.springBoot) version Versions.springBoot apply false
	id(Plugins.liquibase) version Versions.liquibasePlugin apply false
}

allprojects {
	group = "pl.edu.wat.softanet"
	version = "0.0.1-SNAPSHOT"

	repositories {
		mavenCentral()
		maven {
			url = uri("https://maven.jumpmind.com/repo/")
		}
	}

}

subprojects {
	apply(plugin = Plugins.kotlinSpring)
	apply(plugin = Plugins.springDependencyManagement)

	tasks.withType<KotlinCompile>().configureEach {
		kotlinOptions {
			jvmTarget = "11"
			freeCompilerArgs = listOf("-Xjsr305=strict")
		}
	}
	tasks.withType<Test> {
		useJUnitPlatform()
	}

	the<DependencyManagementExtension>().apply {
		imports {
			mavenBom(Dependency.springBootDependencies) { // https://youtrack.jetbrains.com/issue/KT-27994?_ga=2.48821294.945075698.1575373608-807105266.1561545644#focus=streamItem-27-3148043-0-0
				bomProperty("kotlin.version", Versions.kotlin) //
			}
		}
	}
}

