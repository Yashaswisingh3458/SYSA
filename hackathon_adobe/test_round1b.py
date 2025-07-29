import json
import os

# Test the outline loading
output_dir = "app/output"
print(f"Output directory: {output_dir}")
print(f"Files in output: {os.listdir(output_dir)}")

# Try to load an outline
outline_file = "app/output/report cyber.json"
if os.path.exists(outline_file):
    with open(outline_file, 'r', encoding='utf-8') as f:
        outline = json.load(f)
    print(f"Outline loaded successfully")
    print(f"Title: {outline.get('title', 'No title')}")
    print(f"Number of outline items: {len(outline.get('outline', []))}")
    
    # Count sections
    sections = []
    def count_sections(nodes):
        for node in nodes:
            sections.append(node.get('text', ''))
            if node.get('children'):
                count_sections(node['children'])
    
    count_sections(outline.get('outline', []))
    print(f"Total sections found: {len(sections)}")
    print(f"Sample sections: {sections[:5]}")
else:
    print(f"Outline file not found: {outline_file}") 