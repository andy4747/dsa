import os

def generate_md_content(module_name, submodules):
    # Generate the Markdown header
    content = f"# {module_name.capitalize()}\n\n"
    
    for submodule in submodules:
        # Generate Markdown for each submodule
        content += f"## {submodule.capitalize()}\n\n"
        content += f"::: src.{module_name}.{submodule}\n"
        content += ":members:\n\n"
    return content

def create_md_file(filename, content):
    # Create a Markdown file with the generated content
    with open(filename, 'w') as f:
        f.write(content)

def main():
    # Ensure the docs directory exists
    os.makedirs('docs', exist_ok=True)

    # Generate Markdown for algorithms
    algorithms_content = generate_md_content('algorithms', ['searching', 'sorting'])
    create_md_file('docs/algorithms.md', algorithms_content)

    # Generate Markdown for data structures
    data_structures_content = generate_md_content('data_structures', ['linked_list'])
    create_md_file('docs/data_structures.md', data_structures_content)

    # Generate Markdown for leetcode
    leetcode_content = generate_md_content('leetcode.easy', ['rotate_array'])
    create_md_file('docs/leetcode.md', leetcode_content)

    # Generate Markdown for neetcode
    neetcode_content = generate_md_content('neetcode.arrays_and_hashing', ['contains_duplicate'])
    create_md_file('docs/neetcode.md', neetcode_content)

    print("Markdown files generated in the docs directory.")

if __name__ == "__main__":
    main()
