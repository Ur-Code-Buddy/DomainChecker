import whois
import concurrent.futures
from tqdm import tqdm

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status is None:
            return f"{domain} is available."
        else:
            return f"{domain} is not available."
    except whois.parser.PywhoisError:
        return f"Error occurred while checking {domain}."


def sort_domains_alphabetically(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    lines.sort()

    with open(file_path, "w") as sorted_file:
        sorted_file.writelines(lines)


def add_unique_domain(file_path, domain):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    if domain not in lines:
        with open(file_path, "a") as error_file:
            error_file.write(domain + "\n")




# The rest of the functions remain the same


def main():
    filename = "domain_names.txt"
    with open(filename, "r") as file:
        domain_names = file.read().splitlines()

    total_domains = len(domain_names)

    if total_domains == 0:
        print("No domains found in the 'domain_names.txt' file.")
        return

    available_domains = []
    error_domains = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit domain availability check tasks
        future_to_domain = {executor.submit(check_domain_availability, domain): domain for domain in domain_names}

        with tqdm(total=total_domains, desc="Checking domains") as pbar:
            for future in concurrent.futures.as_completed(future_to_domain):
                domain = future_to_domain[future]
                result = future.result()
                if pbar.n > 0:  # Check if the progress is greater than zero to avoid division by zero
                    pbar.set_postfix_str(f"ETA: {pbar.format_dict['elapsed'] / pbar.n * (total_domains - pbar.n):.2f}s")
                pbar.update(1)

                if "available" in result:
                    available_domains.append(domain)
                elif "Error occurred" in result:
                    error_domains.append(domain)

    with open("possible_domain.txt", "a") as error_file:
        for domain in error_domains:
            add_unique_domain("possible_domain.txt", domain)

    print("\nError domains saved to 'possible_domain.txt'")
    print("Taken .com domains:", available_domains)
    print("Number of taken domains:", len(available_domains))
    print("Number of available domains:", len(error_domains))

    # Sort the domains in the file alphabetically
    sort_domains_alphabetically("possible_domain.txt")


if __name__ == "__main__":
    main()