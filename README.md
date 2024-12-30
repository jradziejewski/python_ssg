# Python Static Site Generator

A static site generator that converts markdown files into a served website.

[Watch the video](https://www.youtube.com/watch?v=9Ho-ZutebWs)

## Features
- Converts markdown files to HTML
- Supports nested folder structure for subpages
- Serves the generated site locally
- Copies static assets (images, CSS, etc.)
- Uses customizable HTML template

## Prerequisites
- Python 3.x
- Required Python packages (installed automatically by the script)

## Setup and Usage

1. Clone the repository:
```bash
git clone https://github.com/jradziejewski/python_ssg.git
cd python_ssg
```

2. Add your content:
   - Place markdown (.md) files in the `content` directory
   - Add static assets (images, CSS, JS) to the `static` directory
   - Customize `template.html` in root directory to define page layout
   - Create subdirectories for nested pages if desired
   - Example structure:
   ```
   content/
   ├── index.md
   ├── about.md
   └── blog/
       ├── post1.md
       └── post2.md
   ```

3. Run the generator:
```bash
./main.sh
```

4. Access your site:
   - Open your browser and navigate to `http://localhost:8888`
   - Your markdown files will be served as formatted HTML pages

## File Structure
```
python_ssg/
├── content/        # Place your markdown files here
├── static/         # Static assets (images, CSS, JS)
├── template.html   # HTML template for all pages
├── main.sh         # Main script to run the generator
└── src/            # Source code for the generator
```

## Contributing

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
