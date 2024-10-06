import os

def generate_rst_content(module_name, submodules):
    content = f"{module_name.capitalize()}\n"
    content += "=" * len(module_name) + "\n\n"
    
    for submodule in submodules:
        content += f"{submodule.capitalize()}\n"
        content += "-" * len(submodule) + "\n"
        content += f".. automodule:: src.{module_name}.{submodule}\n"
        content += "   :members:\n\n"
    
    return content


def create_rst_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    # Ensure the docs directory exists
    os.makedirs('docs', exist_ok=True)

    # Generate RST for algorithms
    algorithms_content = generate_rst_content('algorithms', ['searching', 'sorting'])
    create_rst_file('docs/algorithms.rst', algorithms_content)

    # Generate RST for data structures
    data_structures_content = generate_rst_content('data_structures', ['linked_list'])
    create_rst_file('docs/data_structures.rst', data_structures_content)

    # Generate RST for leetcode
    leetcode_content = generate_rst_content('leetcode.easy', ['rotate_array'])
    create_rst_file('docs/leetcode.rst', leetcode_content)

    # Generate RST for neetcode
    neetcode_content = generate_rst_content('neetcode.arrays_and_hashing', ['contains_duplicate'])
    create_rst_file('docs/neetcode.rst', neetcode_content)

    print("RST files generated in the docs directory.")

if __name__ == "__main__":
    main()
