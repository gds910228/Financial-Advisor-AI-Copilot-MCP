# 🚀 Financial Advisor AI Copilot - 部署指南

## 📋 部署概述

本文档提供了金融顾问AI助手MCP服务的完整部署指南，包括环境配置、依赖安装、服务启动和监控等。

## 🔧 系统要求

### 最低配置
- **操作系统**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Python版本**: 3.10 或更高
- **内存**: 4GB RAM
- **存储**: 2GB 可用空间
- **网络**: 稳定的互联网连接（用于市场数据获取）

### 推荐配置
- **操作系统**: Windows 11, macOS 12+, Ubuntu 20.04+
- **Python版本**: 3.11+
- **内存**: 8GB RAM
- **存储**: 5GB 可用空间
- **CPU**: 4核心或更多

## 📦 环境准备

### 1. Python环境安装

#### Windows
```powershell
# 下载并安装Python 3.11
# 从 https://python.org 下载官方安装包
# 确保勾选 "Add Python to PATH"

# 验证安装
python --version
pip --version
```

#### macOS
```bash
# 使用Homebrew安装
brew install python@3.11

# 或使用官方安装包
# 从 https://python.org 下载

# 验证安装
python3 --version
pip3 --version
```

#### Ubuntu/Debian
```bash
# 更新包列表
sudo apt update

# 安装Python 3.11
sudo apt install python3.11 python3.11-pip python3.11-venv

# 验证安装
python3.11 --version
pip3.11 --version
```

### 2. 项目下载

```bash
# 克隆项目（如果使用Git）
git clone <repository-url>
cd mcp5

# 或直接下载项目文件包并解压
```

## 🔨 依赖安装

### 方法1: 使用uv（推荐）

```bash
# 安装uv包管理器
pip install uv

# 安装项目依赖
uv sync

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows
```

### 方法2: 使用pip

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate   # Linux/macOS
# 或
venv\Scripts\activate      # Windows

# 升级pip
pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt
```

### 依赖列表验证

运行以下命令验证所有依赖是否正确安装：

```bash
python test_basic.py
```

预期输出：
```
🧪 Basic Dependency Test
==================================================
✅ Basic Python modules imported successfully
✅ MCP module imported successfully
✅ Pydantic imported successfully
✅ NumPy and Pandas imported successfully

📊 Results: 4/4 tests passed
🎉 All basic tests passed!
```

## 🚀 服务启动

### 1. 配置检查

```bash
# 检查配置文件
python -c "from config import config; print('Config loaded successfully')"
```

### 2. 启动MCP服务器

```bash
# 启动服务器
python main.py
```

服务器启动成功后，您应该看到类似输出：
```
🏦 Financial Advisor AI Copilot MCP Server
Server initialized successfully
Available tools: 6
- create_client_profile
- get_market_data
- build_portfolio
- adjust_portfolio
- backtest_portfolio
- generate_investment_report
```

### 3. 验证服务状态

在另一个终端窗口运行：

```bash
# 运行完整测试套件
python test_mcp_server.py
```

## 🔍 测试和验证

### 基础功能测试

```bash
# 1. 基础依赖测试
python test_basic.py

# 2. 数据模型测试
python demo_mcp_tools.py

# 3. MCP工具测试
python test_mcp_tools_properly.py

# 4. 完整功能测试
python test_mcp_server.py
```

### 预期测试结果

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

## 🐳 Docker部署（可选）

### 1. 创建Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口（如果需要HTTP接口）
EXPOSE 8000

# 启动命令
CMD ["python", "main.py"]
```

### 2. 构建和运行

```bash
# 构建镜像
docker build -t financial-advisor-mcp .

# 运行容器
docker run -p 8000:8000 financial-advisor-mcp
```

## 🔧 生产环境配置

### 1. 环境变量配置

创建 `.env` 文件：

```env
# 数据源配置
ALPHA_VANTAGE_API_KEY=your_api_key_here
FINNHUB_API_KEY=your_api_key_here

# 服务配置
MCP_SERVER_HOST=0.0.0.0
MCP_SERVER_PORT=8000
LOG_LEVEL=INFO

# 缓存配置
ENABLE_CACHE=true
CACHE_TTL=300

# 速率限制
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=3600
```

### 2. 日志配置

```python
# 在config.py中添加日志配置
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('financial_advisor.log'),
        logging.StreamHandler()
    ]
)
```

### 3. 进程管理（使用systemd）

创建 `/etc/systemd/system/financial-advisor-mcp.service`：

```ini
[Unit]
Description=Financial Advisor AI Copilot MCP Service
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/mcp5
Environment=PATH=/path/to/mcp5/venv/bin
ExecStart=/path/to/mcp5/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable financial-advisor-mcp
sudo systemctl start financial-advisor-mcp
sudo systemctl status financial-advisor-mcp
```

## 📊 监控和维护

### 1. 健康检查

创建健康检查脚本 `health_check.py`：

```python
#!/usr/bin/env python3
import requests
import sys

def health_check():
    try:
        # 检查服务状态
        response = requests.get('http://localhost:8000/health', timeout=5)
        if response.status_code == 200:
            print("✅ Service is healthy")
            return 0
        else:
            print(f"❌ Service unhealthy: {response.status_code}")
            return 1
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(health_check())
```

### 2. 日志监控

```bash
# 查看实时日志
tail -f financial_advisor.log

# 查看错误日志
grep ERROR financial_advisor.log

# 日志轮转配置
sudo logrotate -d /etc/logrotate.d/financial-advisor
```

### 3. 性能监控

```bash
# 监控CPU和内存使用
top -p $(pgrep -f "python main.py")

# 监控网络连接
netstat -tulpn | grep :8000
```

## 🚨 故障排除

### 常见问题

#### 1. 依赖安装失败

```bash
# 清理pip缓存
pip cache purge

# 升级pip和setuptools
pip install --upgrade pip setuptools wheel

# 重新安装依赖
pip install -r requirements.txt --force-reinstall
```

#### 2. 市场数据API限制

```bash
# 检查API配额
python -c "import yfinance as yf; print(yf.Ticker('AAPL').info)"

# 使用备用数据源
# 在config.py中配置多个数据源
```

#### 3. 内存不足

```bash
# 监控内存使用
free -h

# 优化Python内存
export PYTHONHASHSEED=0
export PYTHONOPTIMIZE=1
```

#### 4. 端口占用

```bash
# 查找占用端口的进程
lsof -i :8000

# 终止进程
kill -9 <PID>
```

### 日志分析

```bash
# 查看启动日志
grep "Server initialized" financial_advisor.log

# 查看错误统计
grep -c ERROR financial_advisor.log

# 查看API调用统计
grep "API call" financial_advisor.log | wc -l
```

## 🔄 更新和维护

### 1. 代码更新

```bash
# 停止服务
sudo systemctl stop financial-advisor-mcp

# 更新代码
git pull origin main

# 更新依赖
pip install -r requirements.txt --upgrade

# 重启服务
sudo systemctl start financial-advisor-mcp
```

### 2. 数据库维护（如果使用）

```bash
# 备份数据
python -c "from config import backup_data; backup_data()"

# 清理缓存
python -c "from config import clear_cache; clear_cache()"
```

### 3. 定期维护任务

创建cron任务：

```bash
# 编辑crontab
crontab -e

# 添加维护任务
0 2 * * * /path/to/mcp5/venv/bin/python /path/to/mcp5/maintenance.py
0 0 * * 0 /path/to/mcp5/scripts/weekly_cleanup.sh
```

## 📞 技术支持

如果遇到部署问题，请检查：

1. **系统要求** - 确保满足最低配置要求
2. **网络连接** - 确保可以访问外部API
3. **权限设置** - 确保有足够的文件和网络权限
4. **日志文件** - 查看详细错误信息
5. **测试结果** - 运行完整测试套件

---

**部署成功后，您的金融顾问AI助手MCP服务就可以为金融分析师提供专业的投资决策支持了！** 🎉