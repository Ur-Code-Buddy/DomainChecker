Domain Availability Checker

This script is designed to check the availability of domain names provided in the domain_names.txt file. It utilizes the whois library to check the status of each domain and outputs the results.
Prerequisites

    Python 3.x
    Required packages: whois, concurrent.futures, tqdm

Usage

    Make sure you have Python and the required packages installed.
    Create a file named domain_names.txt and add the domain names, each on a separate line.
    Run the script, and it will check the availability of each domain in the list.
    The results will be displayed in the terminal, and available domains will be saved in the possible_domain.txt file.

Code Explanation

    check_domain_availability(domain): A function that checks the availability of a given domain using the whois library. If the domain is available, it returns a message stating that the domain is available; otherwise, it returns a message indicating that the domain is not available or an error occurred during the check.

    sort_domains_alphabetically(file_path): A function that sorts the domain names in the provided file (file_path) alphabetically.

    add_unique_domain(file_path, domain): A function that adds a unique domain to the provided file (file_path). If the domain already exists in the file, it will not be added again.

    main(): The main function that orchestrates the domain availability check. It reads the domain names from the domain_names.txt file, checks their availability concurrently using ThreadPoolExecutor, and saves the available domains to possible_domain.txt. Additionally, it displays the number of taken and available domains.

Note

    Please make sure to respect domain availability restrictions and legalities while using this script.
    For additional functionality or customizations, feel free to modify the code as needed.

Happy domain checking!
