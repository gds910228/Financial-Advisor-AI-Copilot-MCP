# 🏦 Financial Advisor AI Copilot MCP Service

一个基于MCP协议的智能投资顾问服务，为金融分析师提供AI驱动的投资策略协助。

## 🎯 项目概述

本项目是为蓝耘科技MCP挑战赛开发的**领域型服务**，专门针对金融投资领域的专业需求，提供智能化的投资组合管理和风险分析功能。

### 核心特性

- 🤖 **自然语言交互** - 支持中文投资咨询对话
- 👤 **客户档案管理** - 风险偏好和投资目标分析
- 📊 **智能资产配置** - 基于现代投资组合理论(MPT)的优化算法
- 📈 **多数据源集成** - yfinance、Alpha Vantage、Finnhub等
- 🔍 **回测分析** - 历史数据回测和性能指标计算
- 📄 **投资报告生成** - 专业的PDF投资建议报告

## 🚀 快速开始

### 环境要求

- Python 3.10+
- Windows/macOS/Linux

### 安装依赖

```bash
# 使用 uv (推荐)
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### 启动MCP服务器

```bash
python main.py
```

### 运行测试

```bash
# 基础依赖测试
python test_basic.py

# 完整功能测试
python test_mcp_server.py

# MCP工具演示
python demo_mcp_tools.py

# MCP客户端测试
python test_mcp_tools_properly.py
```

## 🔧 MCP工具列表

| 工具名称 | 功能描述 | 参数 |
|---------|---------|------|
| `create_client_profile` | 创建客户投资档案 | name, age, risk_tolerance, investment_horizon, monthly_income, investment_goals, existing_assets |
| `get_market_data` | 获取市场数据 | symbols, period |
| `build_portfolio` | 构建优化投资组合 | client_name, symbols, investment_amount, risk_level |
| `adjust_portfolio` | 调整投资组合 | portfolio_id, instructions |
| `backtest_portfolio` | 回测投资组合 | symbols, weights, start_date, end_date, initial_investment |
| `generate_investment_report` | 生成投资报告 | client_name, portfolio_symbols, portfolio_weights, report_type |

## 📊 使用示例

### 创建客户档案

```python
# 通过MCP工具创建客户档案
result = await session.call_tool("create_client_profile", {
    "name": "张三",
    "age": 35,
    "risk_tolerance": "moderate",
    "investment_horizon": 10,
    "monthly_income": 15000.0,
    "investment_goals": ["retirement", "wealth_growth"],
    "existing_assets": {"cash": 50000, "stocks": 100000}
})
```

### 构建投资组合

```python
# 基于客户档案构建优化投资组合
result = await session.call_tool("build_portfolio", {
    "client_name": "张三",
    "symbols": ["AAPL", "GOOGL", "MSFT", "SPY"],
    "investment_amount": 100000,
    "risk_level": "moderate"
})
```

### 回测分析

```python
# 回测投资组合历史表现
result = await session.call_tool("backtest_portfolio", {
    "symbols": ["AAPL", "GOOGL", "MSFT"],
    "weights": [0.4, 0.3, 0.3],
    "start_date": "2023-01-01",
    "end_date": "2024-01-01",
    "initial_investment": 100000
})
```

## 🏗️ 项目架构

```
mcp5/
├── main.py                 # MCP服务器主入口
├── config.py              # 配置管理
├── models.py              # 数据模型定义
├── test_mcp_server.py     # 综合测试套件
├── demo_mcp_tools.py      # 功能演示
├── examples/              # 使用示例
│   ├── basic_workflow.py
│   ├── advanced_scenarios.py
│   └── run_examples.py
├── docs/                  # 文档
│   ├── PRD.md
│   └── tasks.md
└── pyproject.toml         # 项目配置
```

## 🧪 测试结果

最新测试结果显示：

```
🏁 TEST SUMMARY
=================================================================
Dependencies.................. ✅ PASS
Configuration................. ✅ PASS  
Data Models................... ✅ PASS
Market Data Access............ ⚠️  RATE LIMITED (正常)
Server Startup................ ✅ PASS

Overall: 4/5 tests passed
```

## 🎯 比赛优势

### 1. 领域专业性
- 专门针对金融投资领域设计
- 集成现代投资组合理论(MPT)
- 支持多种风险评估模型

### 2. 技术创新
- 完整的MCP协议实现
- 多数据源适配器架构
- 自然语言处理集成

### 3. 实用价值
- 解决金融分析师日常痛点
- 提供端到端投资决策支持
- 支持中文金融术语和场景

### 4. 可扩展性
- 模块化架构设计
- 支持新数据源接入
- 可集成更多AI模型

## 🔮 未来规划

- [ ] 集成更多数据源(Bloomberg, Reuters)
- [ ] 添加ESG投资策略
- [ ] 支持加密货币投资组合
- [ ] 集成实时风险监控
- [ ] 添加机器学习预测模型

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

**为蓝耘科技MCP挑战赛开发 | 2025年**