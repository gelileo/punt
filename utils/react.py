import subprocess
import os
import re


def start(app_name, tailwind=False):
    # Step 1: Create a new React app
    subprocess.run(["npx", "create-react-app", app_name], check=True)

    # Change directory to the newly created app
    os.chdir(app_name)
    print("switched to: " + os.getcwd())
    print()

    # Step 2: Install Tailwind CSS
    if tailwind:
        subprocess.run(["npm", "install", "tailwindcss"], check=True)
        subprocess.run(["npx", "tailwindcss", "init"], check=True)
        # Step 3: Configure your template paths in tailwind.config.js

        config_path = "./tailwind.config.js"

        # Read the original content of the file
        with open(config_path, "r") as file:
            content = file.read()

        # Replace the content array with the new paths
        new_content = re.sub(
            r"content: \[\],",
            'content: [\n  "./src/**/*.{js,jsx,ts,tsx}",\n],',
            content,
            flags=re.MULTILINE,
        )

        # Write the modified content back to the file
        with open(config_path, "w") as file:
            file.write(new_content)

        # Step 4: Add the Tailwind directives to your CSS
        with open("./src/index.css", "w") as f:
            f.write(
                """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""
            )
        # Step 5: Add import statement for 'index.css' in App.js
        app_js_path = "./src/App.js"
        with open(app_js_path, "r") as file:
            original_content = file.read()
        with open(app_js_path, "w") as file:
            file.write("import './index.css';\n" + original_content)

        os.chdir("..")
    # Step 6: Start your build process
    print(
        f"""
Setup complete. Now you can do the following to start the development server

cd {app_name}
npm start 
"""
    )
