# RL_Based_MultiAgent_Trading_Systems
Multi-Agent Deep Q-Learning Based Trading System with Centralized Reward Optimization
 
🧩 Project Overview:
This project aims to build a multi-agent reinforcement learning (MARL) trading system where each agent is powered by a Deep Q-Network (DQN). Each agent learns to trade independently in a simulated market environment using candlestick chart data and technical indicators. The system applies a centralized reward mechanism to encourage cooperative strategies that collectively maximize portfolio profit. Agents are trained on historical market data and evaluated on back testing and live data streams.

📁 Project Folder: RL_Based_MultiAgent_Trading_Systems/
multiagent-dqn-trader/
├── agents/
│   ├── dqn_agent.py
│   ├── replay_buffer.py
│   └── model.py
│
├── env/
│   ├── trading_env.py
│   ├── market_simulator.py
│   └── reward_functions.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── download_data.py
│
├── training/
│   ├── train_agents.py
│   ├── centralized_reward_tracker.py
│   └── config.yaml
│
├── evaluation/
│   ├── evaluate.py
│   └── backtest.py
│
├── deployment/
│   ├── api.py
│   └── live_trading.py
│
├── utils/
│   ├── indicators.py
│   ├── logger.py
│   └── plotter.py
│
├── models/
│   └── (Saved model .pt/.h5 files here)
│
├── notebooks/
│   └── EDA.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore

📁 Folders & Key Files
agents/

dqn_agent.py – DQN agent class (Q-network, epsilon-greedy, action selection)
replay_buffer.py – Experience Replay memory buffer
model.py – Neural network architecture (e.g., CNN or MLP for Q-value estimation)
env/

trading_env.py – Gym-compatible environment for trading simulation
market_simulator.py – Logic for trade execution, position management, market stepping
reward_functions.py – Defines local and centralized reward structures
data/

download_data.py – Script to fetch data from APIs (e.g., Yahoo Finance, Binance)
raw/, processed/ – Store historical and processed data
training/

train_agents.py – Main training loop for multiple agents
centralized_reward_tracker.py – Tracks and computes shared rewards
config.yaml – Configuration file (hyperparameters, model settings, etc.)
evaluation/

evaluate.py – Runs trained models on test data
backtest.py – Backtesting engine to simulate and visualize agent trades
deployment/

api.py – Optional REST API for live inference
live_trading.py – Integrates with a broker for real-time deployment (e.g., Binance API)
utils/

indicators.py – Add RSI, MACD, EMA, Bollinger Bands to data
logger.py – Logging for training and evaluation
plotter.py – Trade visualization and performance plots
models/

Store .pt or .h5 files for trained agents.
notebooks/

EDA.ipynb – Exploratory Data Analysis on market data
Root Files

requirements.txt – List of dependencies (gym, pytorch, numpy, etc.)
README.md – Project overview, setup instructions, usage
.gitignore – Ignore model files, logs, virtual environments


✅ Starter Commands
# Install dependencies
pip install -r requirements.txt

# Train agents
python training/train_agents.py

# Evaluate agents
python evaluation/evaluate.py

# Backtest
python evaluation/backtest.py


