import subprocess

class Libraries:
    def __init__(self):
        pass
    
    def check_necesary_libraries_installed(self):
        for library in self.necesary_libraries:
            if self.check_library_installed(library_name=library):
                print('Library {} is installed'.format(library))
            else:
                print('Library {} missing.'.format(library))
                self.necesary_libraries_installed = False
                return False
            self.necesary_libraries_installed = True
            return True
    
    necesary_libraries = [""]
    necesary_libraries_installed: bool = False
    
    def check_library_installed(self, library_name):
        command = f"dpkg -s {library_name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout.lower()
            if "status: install ok installed" in output:
                return True
        
        return False
            