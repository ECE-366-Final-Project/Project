// Demo API Skeleton, James Ryan
// GPL v3

package local.Demo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoAPI{
	public static void main(String[] args){
		// Start Spring with the args passed to our program on first-run.
		SpringApplication.run(DemoAPI.class, args);
	}

	// Specify an API path to make the request to
	// type `curl localhost:8080/Demo` to make the request
	@GetMapping("/Demo")
	public String hello(@RequestParam(value = "name", defaultValue = "Gamer") String name,
						@RequestParam(value = "name2", defaultValue = "Gamer2") String name2) {
		return String.format("Hello %s and %s!~\n", name, name2);
	}
}

// PARAM FORMATING 
// $curl "localhost:<PORT>/Demo?<param1>=<value>&<param2>=<value>"
// Example:
// $curl "localhost:8080/Demo?name=james&name2=evan"