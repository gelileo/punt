import fire
from lib import react, tailwind


def start_tailwind():
    print("Starting tailwind...")
    tailwind.start()


def start_react(app_name, tailwind=False):
    print("Starting react...")
    react.start(app_name, tailwind)


if __name__ == "__main__":
    fire.Fire(
        {
            "react": start_react,
            "tailwind": start_tailwind,
        }
    )
