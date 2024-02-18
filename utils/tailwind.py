import subprocess
import os


def html_boilerplate():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Tailwind Project</title>
    <link href="../build/styles.css" rel="stylesheet">
</head>
<body>
    <h1>Hello, Tailwind CSS!</h1>
</body>
</html>
"""


def start():
    # Ensure Node.js and npm are installed
    try:
        subprocess.run(["node", "-v"], check=True, stdout=subprocess.PIPE)
        subprocess.run(["npm", "-v"], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Node.js and npm must be installed to continue.")
        exit(1)

    # Project setup
    # project_name = "my-tailwind-project"
    # os.makedirs(project_name, exist_ok=True)
    # os.chdir(project_name)

    # Initialize a new Node.js project
    subprocess.run(["npm", "init", "-y"], check=True)

    # Install Tailwind CSS, PostCSS, and Autoprefixer
    subprocess.run(
        ["npm", "install", "tailwindcss", "postcss", "autoprefixer"], check=True
    )

    # Generate Tailwind and PostCSS config files
    subprocess.run(["npx", "tailwindcss", "init", "-p"], check=True)

    # Create the src directory, CSS and HTML file
    os.makedirs("src", exist_ok=True)
    os.makedirs("build", exist_ok=True)
    with open("src/input.css", "w") as f:
        f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")

    with open("src/index.html", "w") as f:
        f.write(html_boilerplate())

    # Modify package.json to include the build script
    package_json_path = "package.json"
    with open(package_json_path, "r+") as file:
        content = file.read()
        position = content.find('"scripts": {')
        if position != -1:
            build_script = '"build": "tailwindcss -i ./src/input.css -o ./build/styles.css --watch",'
            prettier_script = (
                '"prettier": "npx prettier --write src/**/*.{js,css,html}",'
            )
            content = (
                content[: position + len('"scripts": {')]
                + build_script
                + prettier_script
                + content[position + len('"scripts": {') :]
            )
            file.seek(0)
            file.write(content)
            file.truncate()

    print("Tailwind CSS project setup is complete.")
    print("Run 'npm run build' to build your CSS.")
    print(
        "Your project is ready at 'src/index.html'. Edit this file to start your project."
    )
