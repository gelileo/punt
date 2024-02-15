import fire
from lib import tailwind


def start_tailwind():
    print("Starting tailwind...")
    tailwind.start()


if __name__ == "__main__":
    fire.Fire(
        {
            "tailwind": start_tailwind,
        }
    )
