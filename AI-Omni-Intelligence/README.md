# AI-Omni Intelligence Engine 🚀

本项目是一套全自动化的全球 AI 技术情报追踪与社交媒体内容生产系统。通过多模型级联架构与异步分发协议，实现了从“源头抓取”到“爆款生成”再到“多端推送”的无人值守闭环。

## 🛠️ 技术架构 (Technical Architecture)
本项目不仅是简单的自动化脚本，而是一个完整的工业级 AI 应用矩阵：
- **自动化编排层 (Workflow)**: 基于 **n8n** 实现海量 RSS 源、GitHub Atom 数据的实时监听与初步去重。
- **智能筛选层 (L1 Filter)**: 使用 **DeepSeek-V3** 进行硬核科技价值评估。通过极高性价比的模型进行初筛，过滤 80% 杂讯，显著降低 Token 消耗。
- **深度创作层 (L2 Rewrite)**: 针对优质情报，调用 **GPT-4o** 进行多模态内容重写（支持小红书爆款风格、技术简报风格）。
- **异步分发网关 (Async Gateway)**: 集成 **OpenClaw**，有效解决企业微信、飞书等平台 5 秒响应限制，确保长文本推送 100% 到达。
- **Agentic 开发流**: 核心 Prompts 与架构方案由 **Claude Code** 辅助审计与优化。

## 🌟 核心亮点
1. **模型级联降本增效**: 采用 DeepSeek 初筛 + GPT-4o 精写的双模型方案。
2. **5s 超时攻克**: 通过 OpenClaw 异步处理机制，完美适配 Reasoning 模型（如 DeepSeek-R1）的推理长文本。
3. **爆款文案自动生成**: 内置针对小红书、自媒体引流优化的提示词库，实现从情报到流量的极速转化。

## 📊 Token 消耗场景 (Token Consumption)
- **Agentic Coding**: 使用 Claude Code 进行代码逻辑审计和多文件重构，产生高额 Context 消耗。
- **高频情报流监测**: 24h 不间断处理全球 50+ 技术源，产生大量的文本理解需求。
- **内容矩阵规模化**: 针对多端分发进行长文本创作，对高性能模型 API 存在持续性、高额度依赖。

## 📦 目录说明
- `/backend`: 基于 FastAPI 的数据接收与管理中心。
- `/frontend`: 基于 Vue3 + Tailwind CSS 的情报看板预览。
- `/workflows`: n8n 自动化流程 JSON 定义文件。
- `/prompts`: 核心提示词库（Markdown 格式）。

## 🤝 开发者
- **Identity**: 一人公司 (One-man Company) / 独立开发者
- **Vision**: 构建基于 AI 的全自动化数字资产实验室
