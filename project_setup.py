import os

# Define folder and file structure
structure = {
    "agents": ["dqn_agent.py", "replay_buffer.py", "model.py"],
    "env": ["trading_env.py", "market_simulator.py", "reward_functions.py"],
    "data": {
        "raw": [],
        "processed": [],
        ".": ["download_data.py"]
    },
    "training": ["train_agents.py", "centralized_reward_tracker.py", "config.yaml"],
    "evaluation": ["evaluate.py", "backtest.py"],
    "deployment": ["api.py", "live_trading.py"],
    "utils": ["indicators.py", "logger.py", "plotter.py"],
    "models": [],
    "notebooks": ["EDA.ipynb"]
}

root_files = ["requirements.txt", "README.md", ".gitignore"]


# Function to create folders and files
def create_project_structure(base_dir="multiagent-dqn-trader"):
    os.makedirs(base_dir, exist_ok=True)

    for folder, contents in structure.items():
        if isinstance(contents, dict):  # Nested structure
            for subfolder, files in contents.items():
                full_path = os.path.join(base_dir, folder, subfolder)
                os.makedirs(full_path, exist_ok=True)
                for file in files:
                    open(os.path.join(full_path, file), 'w').close()
        else:
            full_path = os.path.join(base_dir, folder)
            os.makedirs(full_path, exist_ok=True)
            for file in contents:
                open(os.path.join(full_path, file), 'w').close()

    # Create root files
    for file in root_files:
        open(os.path.join(base_dir, file), 'w').close()

    print(f"Project structure created in: {base_dir}/")


# Run the function
create_project_structure()
