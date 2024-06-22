# Importing the necessary module
import subprocess

# Function to check PIP version
def check_pip_version():
    result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
    return result.stdout

# Function to install a package
def install_package(package_name):
    result = subprocess.run(['pip', 'install', package_name], capture_output=True, text=True)
    return result.stdout

# Function to uninstall a package
def uninstall_package(package_name):
    result = subprocess.run(['pip', 'uninstall', package_name, '-y'], capture_output=True, text=True)
    return result.stdout

# Function to list installed packages
def list_installed_packages():
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    return result.stdout

# Main logic of the program
def main():
    # Check PIP version
    print("Checking PIP version:")
    pip_version = check_pip_version()
    print(pip_version)
    
    # Install a package named 'camelcase'
    print("\nInstalling 'camelcase' package:")
    install_result = install_package('camelcase')
    print(install_result)
    
    # List installed packages to confirm installation
    print("\nList of installed packages:")
    installed_packages = list_installed_packages()
    print(installed_packages)
    
    # Import and use 'camelcase' package
    try:
        import camelcase
        c = camelcase.CamelCase()
        txt = "hello world"
        print("\nUsing 'camelcase' package:")
        print(c.hump(txt))
    except ImportError:
        print("\nError importing 'camelcase' package.")
    
    # Uninstall 'camelcase' package
    print("\nUninstalling 'camelcase' package:")
    uninstall_result = uninstall_package('camelcase')
    print(uninstall_result)
    
    # List installed packages to confirm uninstallation
    print("\nList of installed packages:")
    installed_packages = list_installed_packages()
    print(installed_packages)

# Run the main function
if __name__ == "__main__":
    main()
