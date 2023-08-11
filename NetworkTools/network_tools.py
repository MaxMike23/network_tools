import subprocess

def interface_is_connected() -> bool:
    """ A function that determines if network interface is connected to internet """
    result = subprocess.run(["netsh", "interface", "show", "interface"],
                            shell=True,
                            capture_output=True,
                            text=True)

    for line in [line for line in result.stdout.splitlines()]:
        if "Connected" in line:
            result = subprocess.run(["ping", "8.8.8.8"],
                                    shell=True,
                                    capture_output=True
                                    )
            if result.returncode == 0:
                return True

    return False


if __name__ == "__main__":
    print(interface_is_connected())