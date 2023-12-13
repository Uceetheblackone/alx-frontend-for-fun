import argparse
import sys
import os
import markdown2

def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown2.markdown(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('input_file', help='Name of the Markdown file')
    parser.add_argument('output_file', help='Name of the output HTML file')

    args = parser.parse_args()

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    convert_markdown_to_html(args.input_file, args.output_file)
    sys.exit(0)
